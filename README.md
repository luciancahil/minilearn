# minilearn
A quick way to visualize data using TSNE and PCA


## Setup

To setup an environment for this code, run the following commands in your desired conda environment.

```
conda install matplotlib=3.10.3
pip install scikit-learn==1.6.1
pip install pandas==2.2.3
pip install openpyxl==3.1.5
```


## Use

To start off, place the data you want to analyze into the "Data" Folder.


Then, edit the main.py file by changing the following 4 variables


|Variable|Explanation| Example|
|---|---|---|
|name| The name of the file, minus the extension| If your file is data.xlss, set it to "data"|
|input_start|The collumn number (0-indexed) where data for PCA and TSNE start| If you want to analyze the first row to the 10th inclusive, you should set this value to 0
|input_end|The collumn number (0-indexed) where data for PCA and TSNE ends| If you want to analyze the first row to the 10th inclusive, you should set this value to 10
|output_index|The collumn where you store the labels, based on 0-index| If the output variable is stored in the 11th collumn, set this variable to 10 (NOT 11!!).


## Images

Images will all be stored in the "Images" Folder. Each run will generate 2 images, one for TSNE and one for PCA. If you run this file multiple times, new runs will overwrite the images from the old runs.


## Example

To see this library in use, open and run main.py. It currently analyzes randomly generated data in Data/Example.xlsx