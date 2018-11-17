import os
from calest import calest_app

__author__ = "ricardoperezf, gsusfm"
__version__ = "1.0.0"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    calest_app.run(host='0.0.0.0', port=port)