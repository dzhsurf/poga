call conda deactivate

call conda env remove --name poga-py37
call conda env create -f deploy\\conda-env-py37.yaml
call conda activate poga-py37
call python setup.py bdist_wheel
call conda deactivate

call conda env remove --name poga-py38
call conda env create -f deploy\\conda-env-py38.yaml
call conda activate poga-py38
call python setup.py bdist_wheel
call conda deactivate

call conda env remove --name poga-py39
call conda env create -f deploy\\conda-env-py39.yaml
call conda activate poga-py39
call python setup.py bdist_wheel
call conda deactivate

call conda env remove --name poga-py310
call conda env create -f deploy\\conda-env-py310.yaml
call conda activate poga-py310
call python setup.py bdist_wheel

call python setup.py sdist
call conda deactivate


