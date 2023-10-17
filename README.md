# slurmtools

This slurm script allows one to submit a slurm job using a python script.
A python file and two yaml files need to be provided :
- The python script to run (`script.py`).
- The config file to use : provides application specific parameters (`config.yml`).
- The sbatch config file : provides slurm parameters (`sbatch.yml`).\\

On top of that, either conda or pip package management can be used. 
To use a conda virtual environment named `venv`, one needs to provide `conda` argument followed by `--env venv` to specify the environment. 
To use pip with a virtual environnement named, one needs to provide `pip` argument followed by `--requirements requirements.txt` where `requirements.txt` is the wanted requirements file :

```
python code/slurm.py script.py config.yml sbatch.py conda venv
```

To create an alias run the following code :

```
alias slurm="python path/to/code/slurm.py"
```

Then it is possible to submit slurm jobs using the following command line :

```
slurm script.py config.yml sbatch.py conda venv
```