import string
import random


website.renderer_factories['jinja2'].Renderer.global_context = {
    'range': range,
    'unicode': unicode,
    'enumerate': enumerate,
    'len': len,
    'float': float,
    'type': type,
    'str': str,
}

website.renderer_default = "jinja2"


# Set website.version.
# ====================
# Yeesh, what a hack. At Heroku we don't have a git repo once deployed, so
# instead of using a git SHA we're going to just use a random string. Doing
# this "right" would mean storing the real version SHA somewhere during
# deployment.

website.version = ''.join([random.choice(string.letters) for i in range(32)])


# Set random thing that we're not really using.
# =============================================

website.compress_assets = False # If set to True, the responsiveness on the lower
                                # homepage breaks. :-/
