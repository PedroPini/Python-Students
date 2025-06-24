# Python-Students

### ✅ 1. **Install `virtualenv` (if not using `venv`)**

If you're using Python 3.3+, you can use the built-in `venv`. Otherwise, you can install `virtualenv`.


```
pip install virtualenv

python -m venv myenv
```

### ✅ 3. **Activate the Virtual Environment**

- **Windows**:

```
myenv\Scripts\activate
```
  ``

- **Mac/Linux**:
```
source myenv/bin/activate
```

### ✅ 3. **Deactivate the Virtual Environment**

```
deactivate
```

### ✅ 4. Create Environment for `requirements.txt

```
pip freeze > requirements.txt
```
### ✅ 7. **Recreate Environment from `requirements.txt`**

If sharing your project:


```
pip install -r requirements.txt
