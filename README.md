Text_Processing_U.She
=========================
Text Processing which is based on the class in the University of Sheffield.

Build Your Customized Jupyter Notebook Env by Anaconda
=========================
1.Create a new env by Anaconda Command
```
conda create -n <YOUR ENVIRONMENT NAME> python=3.6 
```
2.Install ipykernel on your env
```
conda install -n <YOUR ENVIRONMENT Name> ipykernel
```
3.Activate and Enter the env
```
source ~/.bash_profile
source activate <YOUR Environment Name>
```
4.Write the environment to the kernel of the Jupyter Notebook
```
(<env name>)> python -m ipykernel install --user --name <env name> --display-name "<display env name>"
```
5.Open the Jupyter Notebook
```
(<env name>)> jupyter notebook
```

How to Download the File from Ftp Server
=========================
Thanks to my tutor, you can access the lab data by click [here](https://staffwww.dcs.shef.ac.uk/people/M.Hepple/campus_only/COM6115/python_intro/code_data/).

```sh
$ curl -O target/path/filename URL
```


