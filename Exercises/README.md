# INF8808 Python Exercices

These exercices cover material for INF8808, organized by lab topic. They include Python, Dash, Plotly and Plotly Express exercices. Some TPs will also use Jupyter notebooks so getting familiar with running Jupyter will also be useful. 

## To run the exercices : 

1. Create a python virtualenv
  `virtualenv -p 3.8 env`
  
  2. Activate env
  `source ./env/Scripts/activate` or `source ./env/bin/activate`
  
  3. Install requirements 
  `pip install -r requirements-linux.txt` or  `pip install -r requirements-windows.txt`
  
  4. Create python kernel 
  `ipython kernel install --user --name=tp_kernel`
  
  5. Launch Jupyter
  `jupyter notebook`
  
  6. Once the notebook is opened, select your newly created kernel using the Jupyter notebook interface (Kernel -> Change Kernel -> tp_kernel)
  
  7. Use the Jupyter notebook interface to run the code

  8. **(NOTE)** : If you get a 'modulenotfounderror', make sure your current working directory is correct. In a Jupiter cell at the top of the notebook : 

```
import os
os.getcwd()
```

This checks your current working directory. Change it to the path containing your modules (ex : ./venv/lib/python3.8/site-packages) using for example : `os.chdir('${YOUR_PATH}/site-packages')`
