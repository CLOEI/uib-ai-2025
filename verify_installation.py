import sys
import importlib
package = ['numpy', 'pandas', 'sklearn', 'skfuzzy', 'cv2', 'matplotlib', 'nltk']
for p in package:
    try:
        m = importlib.import_module(p)
        print(f"{p}: OK, Version = {getattr(m, '__version__', 'unknown')}")
    except Exception as e:
        print(f"{p}: ERROR -> {e}")

print('Python:', sys.version)