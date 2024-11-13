from collections import defaultdict
from atproto import models
from server.logger import logger
from server.database import db, Post

def operations_callback(ops: defaultdict) -> None:
    posts_to_create = []
    for created_post in ops[models.ids.AppBskyFeedPost]['created']:
        author = created_post['author']
        record = created_post['record']
        
        # Verifica se o post contém a palavra "Bradesco"
        if 'bradesco' in record.text.lower():
            reply_root = reply_parent = None
            if record.reply:
                reply_root = record.reply.root.uri
                reply_parent = record.reply.parent.uri
            
            post_dict = {
                'uri': created_post['uri'],
                'cid': created_post['cid'],
                'reply_parent': reply_parent,
                'reply_root': reply_root,
            }
            posts_to_create.append(post_dict)
            logger.info(f'Post relacionado ao Bradesco adicionado: {record.text}')

    posts_to_delete = ops[models.ids.AppBskyFeedPost]['deleted']
    if posts_to_delete:
        post_uris_to_delete = [post['uri'] for post in posts_to_delete]
        Post.delete().where(Post.uri.in_(post_uris_to_delete))
        logger.info(f'Deletado do feed: {len(post_uris_to_delete)}')

    if posts_to_create:
        with db.atomic():
            for post_dict in posts_to_create:
                Post.create(**post_dict)
        logger.info(f'Adicionado ao feed: {len(posts_to_create)}')
