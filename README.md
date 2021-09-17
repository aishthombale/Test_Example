**Test Example**
Example folder and having two modules to test two different files, 
**1.example_yaml.py :** 
To read Yaml configurations file and flatten
input: .yaml file path
output: flatten dictionary
**2.example_cfg.py :** 
To read .cfg configurations file and flatten
input: .cfg file path
output: flatten dictionary

**To test these examples you need to perform the following steps:**

1. Download the zip file of project present at below repository,
[https://github.com/aishthombale/config_to_flatdict.git]
   
2.Create new project in Python IDE with name as "example".

3.Create a virtual environment in "example" folder using below command.
`virtualenv example`

4.Activate virtual environment using below command.
`example\scripts\activate`

5.Install wheel file in a virtual environment which you can find
in the project downloaded in step 1 at below path.   
`config_to_flatdict/dist/file_to_flatdict-0.0.1-py3-none-any.whl`

6.Run each of the examples and check the output.
You can use files present in `config` folder as input to the `example_yaml.py` and `example_cfg.py`