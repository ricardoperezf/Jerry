import os
from jerry import jerry_app

__author__ = "ricardoperezf, gsusfm, richardlm57"
__version__ = "1.0.0"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    jerry_app.run(host='0.0.0.0', port=port, debug=True)
