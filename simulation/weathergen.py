# read average weather data and generate realistic random weather

import os
from csvReader import csvReader as csv

from floss.settings import BASE_DIR

test= "---" # print statements preceded with --- are debug statements, these should be deleted in production



# Functions to read particular types of file ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def read_wg_file(filenumber, scenario):
    """
    Reads the Weather gen (wg) files generated by the weather gen programme from UKCP09
    these files follow the naming convention r_<filenumber>_scen_dly.csv where <filenumber>
    is the ID for a given file.

    They are CSV files where , denotes a new cell and a new
    line denotes a new row of the table. The column headings are stored separately from
    the data.

    Returns:
        dict: containing the fields "length", "units" and "headings", as well as fields corresponding
        to each of the headings
    """

    prefix = "r_"
    suffix = "_scen_dly"
    extension = ".csv"
    filename = prefix+'{0:04d}'.format(filenumber)+suffix+extension
    file = os.path.join(BASE_DIR, "simulation", "weather", scenario, filename)

    delim = csv.TableDelimiters(empty_cell="")
    types = csv.DataTypes(types="dt, it, it, it, it, ft, ft, ft, ft, ft, ft, ft, ft, ft")
    lab = csv.Labels(
        headings="year, month, day, day_count, transition, precip_dtotal, temp_dmin, temp_dmax, vapourpressure_dmean, relhum_dmean, sunshine_dtotal, diffradt_dtotal, dirradt_dtotal, pet_dmean",
        units="-, -, -, -, -, mm / day, degC, degC, hPa, %, hours, kWh / m2, kWh / m2, mm / day"
    )
    wg = csv.FileSettings(delimiters=delim, data_types=types, labels=lab)

    text = csv.open_file(file)
    data = csv.read_file(text, wg)
    data = list(zip(*data)) # transpose the data
    data = csv.label(data, lab)
    return data



def read_lw_file():
    """
    reads local weather(lw) from the met office
    these files have 5 lines of explanatory information
    followed by the column headings yyyy mm tmax tmin af rain sun
    followed by the units for each column blank blank degC degC days mm hours
    followed by the data, which may be marked with # or * in some cases, absent data marked ---
    """
    file = csv.choose_file_in_dir()
    text = csv.open_file(file)

    delim = csv.TableDelimiters(cell_border=r"[\s]{2,}", empty_cell=r"---$")
    lab = csv.Labels(heading_row=5, unit_row=6, data_row=7)
    lw = csv.FileSettings(delimiters=delim, labels=lab)
    data = csv.read_file(text, lw)
    sort_col = lab.headings.index("mm")
    data = csv.split_by_values(data, sort_col, [1, 13])
    data = csv.transpose(data, 12)
    return data



#
# try:
#     print(read_lw_file())
# except WeatherError as err:
#     print(err.value, err.info)
# print("done")
#
# try:
#     data=(read_wg_file(1))
# except WeatherError as err:
#     print(err.value, err.info)
#
# for row in data:
#     for group in row:
#         print(group)
# print("done")
