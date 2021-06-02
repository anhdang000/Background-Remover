# OCR Fast Label Tool - Deployment Instruction

Author: Dang Linh Anh

## Branches:

- Master
## Dependencies:

- OS: Ubuntu >= 18 (Recommended)
- PyQt5
- Python 3

<b>Note</b>: When working with Vietnamese, this tool may not work properly in Windows because of some GUI-based conflicts in encoding and decoding texts. 

## Deploy instructions: 

- Step 1: Put your input cropped images (into words) named `crop_img` in the same folder with script files

- Step 2: (Optional) The pre-recognized result file named `rec_gt.txt` must be put at the same folder with script files

- Step 3: To execute the GUI:

```
    usage: label_imgs.py [-h] [--prev-row PREV_ROW] [--num-examples NUM_EXAMPLES]
                     [--num-cols NUM_COLS]

    optional arguments:
      -h, --help            show this help message and exit
      --prev-row PREV_ROW   Previous working row. For resuming.
      --num-examples NUM_EXAMPLES
                            Number of examples will be loaded into the table.
      --num-cols NUM_COLS   Number of main columns.
```    
 

- Step 4: Start labeling! Using Enter key is recommended to traverse quickly to the next text column

- Step 5: (Optional) [Need backup] To clear output files to get ready for a next labeling session:

```
    chmod +x clear_outputfile.sh
    bash clear_outputfile.sh
```    
 

## Interfaces:

The tool is organized into 5 main columns. Each column contains 2 entries named Input and Label.
Buttons: 
- **Submit**: Save all labeled words into `output.txt`. Any texts which are different from the initially loaded ones would be saved into `output_diff.txt`. Duplicated submissions do not change the output file.
- **Clear**: Clear all texts on the working board.
- **Status bar**: Display location of current editing cell for easy tracking.

## Other notes:
- Do not use Tab key for all the time. Because when submitting, the tool makes a recent row at which Enter key is pressed as the current row for saving.
- The pre-recognized result is loaded into rows. The number of examples which are not actually loaded into the table is the remainder part of the calculation of `NUM_EXAMPLES/NUM_COLS`.


> Happy labeling!
