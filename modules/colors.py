# ################################################### #
#                                                     #
#           ..#######..########.##.....##             #
#           .##.....##.##.......##.....##             #
#           ........##.##.......##.....##             #
#           ..#######..######...#########             #
#           .##........##.......##.....##             #
#           .##........##.......##.....##             #
#           .#########.##.......##.....##             #
#                                                     #
#       Facebook checker v2.0 - coded by 2FH          #
#                                                     #
#   Proyecto: Facebook checker                        #
#   Autores: def Empty(): - YaderPR~                  #
#   Grupo: Two Factor Hack (2FH)                      #
#   Hora: 7:17 PM                                     #
#   Fecha: 21 de Julio del 2020.                      #
#                                                     #
# ################################################### #

if (__name__ == "__main__"): exit();      

class Color(object):

    __attr__ = ['azul','rojo','verde','purpura','amarillo','reset','rgb'];
    reset = '\033[0;37m';
    
    def __init__(self, reset = None): 
        
        if (reset is not None): self.reset = reset;

    def __str__(self): return self.reset;

    # Propiedades constantes

    @property
    def azul(self): return '\033[0;34m';
    
    @property
    def rojo(self): return '\033[0;31m';
    
    @property
    def verde(self): return '\033[0;32m';
    
    @property
    def morado(self): return '\033[0;35m';
    
    @property
    def amarillo(self): return '\033[0;33m';

    # Propiedad indeterminada

    def RGB(self,red,green,blue):

        if (red >= 0 and red <= 255):
            
            if (green >= 0 and green <= 255):
                
                if (blue >= 0 and blue <= 255): self.rgb = f'\x1b[38;2;{red};{green};{blue}m';
                else: self.rgb = self.reset;

            else: self.rgb = self.reset;

        else: self.rgb = self.reset;

        return self.rgb;