# ESPIn 2020 Lecture

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/benbovy/espin2020_lecture/master?urlpath=lab)

Jupyter notebooks for CSDMS [ESPIn 2020](https://github.com/csdms/espin) lecture

"A Shallow Overview of the Broader Python Ecosystem for Scientific Modelling"

## How to run the notebooks?

You can try running the notebooks from your browser without installing anything
thanks to [binder](https://mybinder.org/). Just click on the "launch binder"
badge above and it will launch remotely a new notebook server for you. This
service is for demo purpose only, do not rely on it for doing more serious work.
Also it is likely that no computation will happen in parallel (1 CPU only).

Alternatively, you can run the notebook server on your own
machine. Assuming that you have `git` and
[conda](https://conda.io/docs/index.html) installed, you just need to
run the following commands to install and activate the environment:

```
   $ git clone https://github.com/benbovy/espin2020_lecture
   $ cd espin2020_lecture
   $ conda env create -f environment.yml
   $ conda activate fastscape-espin2020 
```

Then run the command below to start the notebook server. It should open
a new tab in your browser.

```
    $ jupyter notebook
```
