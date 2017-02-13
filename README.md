# python-lesson-study
python 自学练习

### 在项目跟目录下面执行，创建虚拟环境<br />
安装：  <br />
    brew install pyenv  <br />

安装virtualenv：<br />
    git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv <br />

配置环境变量：<br />
    export PYENV_ROOT="$HOME/.pyenv"  <br />
    export PATH="$PYENV_ROOT/bin:$PATH"  <br />
    eval "$(pyenv init -)"  <br />
    eval "$(pyenv virtualenv-init -)" <br />

安装python版本、设置虚拟环境：<br />
    1: pyenv install 2.7.10<br />
    2: pyenv virtualenv 2.7.10 venv-2.7.10<br />
    3: pyenv versions<br />
    4: pyenv activate venv-2.7.10   激活venv-2.7.10 虚拟环境<br />
       此时查看python version是2.7.10<br />

    5: pip install -r requirements.txt   安装工程需要的依赖 <br />
    6: export FLASK_APP=index.py <br />
    7: flask run <br />

停用虚拟环境：    <br />
    1: pyenv deactivate venv-2.7.10      停用 venv-2.7.10 虚拟环境<br />
