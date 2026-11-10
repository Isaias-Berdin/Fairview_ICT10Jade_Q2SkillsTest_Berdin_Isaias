from pyscript import document

element = {
    "H" : ("Hydrogen", 1.008, 1),
    "He" : ("Helium", 4.003, 8),
    "C" : ("Carbon", 12.01, 4),
    "N" : ("Nitrogen", 14.01, 5),
    "O" : ("Oxygen", 16, 6),
    "F" : ("Fluorine", 19, 7),
    "Ne" : ("Neon", 20.18, 8),
    "P" : ("Phosphorus", 30.98, 5),
    "S" : ("Sulfur", 32.07, 6),
    "Cl" : ("Chlorine", 35.45, 7),
    "Ar" : ("Argon", 39.95, 8),
    "Se" : ("Selenium", 78.96, 6),
    "Br" : ("Bromine", 79.9, 7),
    "Kr" : ("Krypton", 83.8, 8),
    "I" : ("Iodine", 126.9, 7),
    "Xe" : ("Xenon", 131.3, 8),
    "Rn" : ("Radon", 22, 8)
}
   
def verify_element(e):
    element_name = document.getElementById("symbol").value.strip().title()
         
    var2 = element.get(element_name,("Element Not Found","-","-"))   

    document.getElementById("output1").innerHTML = f"""
        Symbol: {element_name}<br>
        Element: {var2[0]}<br>
        Group Number: {var2[2]}<br>
        Atomic Mass: {var2[1]}<br>
    """ 

    
