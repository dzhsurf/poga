call conda deactivate
call conda env remove --name poga-py37
call conda env create -f deploy\conda-env-py37.yaml
call conda activate poga-py37
call poetry config virtualenvs.create false 
call poetry env use python
call poetry build --format=wheel
call conda deactivate

call conda env remove --name poga-py38
call conda env create -f deploy\conda-env-py38.yaml
call conda activate poga-py38
call poetry config virtualenvs.create false 
call poetry env use python
call poetry build --format=wheel
call conda deactivate

call conda env remove --name poga-py39
call conda env create -f deploy\conda-env-py39.yaml
call conda activate poga-py39
call poetry config virtualenvs.create false 
call poetry env use python
call poetry build --format=wheel
call conda deactivate

call conda env remove --name poga-py310
call conda env create -f deploy\conda-env-py310.yaml
call conda activate poga-py310
call copy /y %CONDA_PREFIX%\Library\bin\ffi.dll %CONDA_PREFIX%\ffi.dll
call copy /y %CONDA_PREFIX%\Library\bin\ffi-7.dll %CONDA_PREFIX%\ffi-7.dll
call copy /y %CONDA_PREFIX%\Library\bin\ffi-8.dll %CONDA_PREFIX%\ffi-8.dll
call copy /y %CONDA_PREFIX%\Library\bin\libssl-1_1.dll %CONDA_PREFIX%\libssl-1_1.dll
call copy /y %CONDA_PREFIX%\Library\bin\libcrypto-1_1.dll %CONDA_PREFIX%\libcrypto-1_1.dll
call copy /y %CONDA_PREFIX%\Library\bin\libssl-3-x64.dll %CONDA_PREFIX%\libssl-3-x64.dll
call copy /y %CONDA_PREFIX%\Library\bin\libcrypto-3-x64.dll %CONDA_PREFIX%\libcrypto-3-x64.dll
call poetry config virtualenvs.create false 
call poetry env use python
call poetry build --format=wheel
call conda deactivate



