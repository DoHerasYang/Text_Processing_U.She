Text_Processing_U.She
=========================
**Text Processing which is based on the class in the University of Sheffield.**

<img src="./pictures/NLP-wordcloud.png" alt="logo" style="zoom: 50%;" />

![](/Users/doheras/Desktop/Text Processing/Text_Processing_U.She/pictures/University-of-Sheffield-2010.jpg) 

# How to quickly import the Anaconda environment

1. Move to your directory where the `$directory` you want to install and extract the `textprocessing.yml` and `requirement.txt` into your current terminal path. Then, follow the instruction below: 
```shell
$ conda env create -f textprcessing.yml
$ pip install -r requirement.txt
```
2. If you wish to use your own name for your env, follow these instruction below:
```shell
$ conda create --name <YOUR ENVIRONMENT NAME> --clone textprocessing
# Please make sure you don't have env with same name
$ conda remove --name textprocessing --all
```


Build Your Customized Jupyter Notebook Env by Anaconda
=========================

1.Install ipykernel on your env

```shell
conda install -n <YOUR ENVIRONMENT Name> ipykernel
```
2.Activate and Enter the env

```shell
source ~/.bash_profile
source activate <YOUR Environment Name>
```
3.Write the environment to the kernel of the Jupyter Notebook

```shell
(<env name>)> python -m ipykernel install --user --name <env name> --display-name "<display env name>"
```
4.Open the Jupyter Notebook

```
(<env name>)> jupyter notebook
```

How to Download the File from Ftp Server
=========================
Thanks to my tutor, you can access the lab data by click [here](https://staffwww.dcs.shef.ac.uk/people/M.Hepple/campus_only/COM6115/python_intro/code_data/).

```sh
$ curl -O target/path/filename URL
```


