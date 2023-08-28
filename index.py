import PySimpleGUI as sg
layout = [
  [
    sg.Input(key= '-INPUT-'),
    sg.Spin(['Km to mile','Kg to pound','sec to min'], key ='-UNITS'),
    sg.Button('Convert',key = '-CONVERT-')
 ],
 [sg.Text('Output',key = '-OUTPUT-')] 
]  
window =sg.Window('Converter ✨',layout)

while True:
    event,values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    if event == '-CONVERT-':
      input_value = values['-INPUT-']
      if input_value.isnumeric():
            match values['-UNITS']:
                case 'Km to mile':
                    output = round(float(input_value)*0.6214,2)
                    output_string = f'{input_value} Km are {output} miles. '
                
                case 'Kg to pound':
                    output = round(float(input_value)*2.20462,2)
                    output_string = f'{input_value} Kg are {output} pounds. '
                    
                case 'sec to min':
                    output = round(float(input_value)/60,2)
                    output_string = f'{input_value} seconds are {output} minutes. '
                    
            window['-OUTPUT-'].Update(output_string)        
   
                    
window.close()  
