'''
MIT License

Copyright (c) 2020 Sebastian Cornejo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

"""
Los productos que salen del reporte diario son:
7
8
9
10
12
17
20
23
24
"""

import pandas as pd
import utils
from shutil import copyfile


def prod7_8(fte, producto):
    df = pd.read_csv(fte, dtype={'Codigo region': object})
    utils.regionName(df)
    df_t = df.T
    df.to_csv(producto + '.csv', index=False)
    df_t.to_csv(producto + '_T.csv', header=False)


def prod9_10_20_23_24(fte, producto):
    copyfile(fte, producto + '.csv')
    HospitalizadosUCIEtario_T = utils.transpone_csv(producto + '.csv')
    HospitalizadosUCIEtario_T.to_csv(producto + '_T.csv', header=False)


if __name__ == '__main__':
    print('Generando producto 7')
    prod7_8('../input/ReporteDiario/PCR.csv', '../output/producto7/PCR')

    print('Generando producto 8')
    prod7_8('../input/ReporteDiario//UCI.csv', '../output/producto8/UCI')

    print('Generando producto 9')
    prod9_10_20_23_24('../input/ReporteDiario/HospitalizadosUCIEtario.csv', '../output/producto9/HospitalizadosUCIEtario')

    print('Generando producto 10')
    prod9_10_20_23_24('../input/ReporteDiario/FallecidosEtario.csv', '../output/producto10/FallecidosEtario')

    print('Generando producto 12')
    exec(open('bulk_producto7.py').read())

    print('Generando producto 17')
    copyfile('../input/ReporteDiario/PCREstablecimiento.csv', '../output/producto17/PCREstablecimiento.csv')

    print('Generando producto 20')
    prod9_10_20_23_24('../input/ReporteDiario/NumeroVentiladores.csv', '../output/producto20/NumeroVentiladores')

    print('Generando producto 23')
    prod9_10_20_23_24('../input/ReporteDiario/PacientesCriticos.csv', '../output/producto23/PacientesCriticos')

    print('Generando producto 24')
    prod9_10_20_23_24('../input/ReporteDiario/CamasHospital_Diario.csv', '../output/producto24/CamasHospital_Diario')
