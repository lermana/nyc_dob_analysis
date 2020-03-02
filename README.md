# nyc_dob_analysis

## Overview

This repository corresponds to the open-source analysis conducted by [NewTrails Data Science](http://newtrails.io) that covers the New York City Department of Buildings, and contains:
- a Python library, `pydob`, which we've written for downloading, ingesting, and analyzing the DoB data
- a collection of Jupyter notebooks that were used to generate the charts in our report
- the figures that we chose to include in our report
- the report itself, in markdown form

Below you will find the [executive summary](#executive-summary) for our report and the [setup instructions](#setup-instructions) for making use of our Python code.

## Executive Summary

- put here once done

## Setup Instructions

#### `pydob`

To install `pydob` simply run the following, once you've cloned this repository:
 ```
 cd pydob
 pip install .
 ```

You can see find the required and auto-installed dependencies [here](pydob/setup.py#L10).

#### `DOB_DATA_DIR`

This code relies upon the setting of an environment variable named `DOB_DATA_DIR`, whose value is assumed to be the location in which should be kept all the data generated by and required for, the running of our code.

The default behavior - which the program will notify you of once it is running - can be avoided through setting this variable prior to running the code (you can also see the default behavior for yourself, [here](pydob/pydob/settings.py#L13)). If you do not set this variable in your environment, the program will ask for permission before doing anything, providing you with the opportunity to kill the program, set this variable, and run again.

Finally, the program will create a new folder (a sub-directory of `DOB_DATA_DIR`) to store the programmatically generated figures in - we've left our final figures where they are in this repo so that they are conveniently viewable.

#### `build`

Once `pydob` has been installed and `DOB_DATA_DIR` set to your liking, you are ready to run the program:
```
from pydob.build import build
build()
```
Note that, if you choose to rerun at some point (maybe due to network issues or your making of modifications to the code) you can pass `use_existing=True` to `build` to avoid re-downloading any DoB data that is already available in `DOB_DATA_DIR`.

Also note that the DoB datasets each span roughly 1-2+M rows and 20-50 columns, which means that running `build` may take upwards of an hour and may require significant computational capacity from your local machine.
