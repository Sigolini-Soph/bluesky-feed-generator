import os

SERVICE_DID = os.environ.get('SERVICE_DID', None)
HOSTNAME = os.environ.get('HOSTNAME', None)

if HOSTNAME is None:
    raise RuntimeError('You should set "HOSTNAME" environment variable first.')

if SERVICE_DID is None:
    SERVICE_DID = f'did:web:{HOSTNAME}'

# URI do feed ALF
WHATS_ALF_URI = os.environ.get('WHATS_ALF_URI')
if WHATS_ALF_URI is None:
    raise RuntimeError('Publish your feed first (run publish_feed.py) to obtain Feed URI. '
                       'Set this URI to "WHATS_ALF_URI" environment variable.')

# URI do feed Bradesco
WHATS_BRADESCO_URI = os.environ.get('WHATS_BRADESCO_URI')
if WHATS_BRADESCO_URI is None:
    raise RuntimeError('Publish your Bradesco feed first (run publish_feed.py) to obtain Feed URI. '
                       'Set this URI to "WHATS_BRADESCO_URI" environment variable.')

