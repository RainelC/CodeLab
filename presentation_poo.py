# Realizar una presentación donde usted va a exponer con sus palabras  los siguientes conceptos de la programación orientada a objetos.

# Abstracción
# Encapsulamiento ✅
# Herencia ✅
# Polimorfismo ✅   
# Clase ✅ 
# Objeto ✅ 
# Clase Abstracta ✅ 
# Interface.
# Métodos virtuales
# Método constructor
# Sobrecarga de métodos.


# Conceptos de la programación orientada a objetos.

def Encapsulamiento():

    concepto = """
        El encapsulamiento es la manera en la que en una clase se puede regular el acceso a sus atributos y metodos, existen 
        varios tipos de acceso entre ellos "Public", "Private" y "Protected" 
        """
    
    explicacionTipos = """  
        Los tipos de acceso se explican solo:
         
        "Public" Las clases o atributos con este acceso estarán disponibles desde cualquier parte del proyecto, tanto en otras clases 
         como en otros paquetes.

        "Protected" Las clases o atributos con este acceso solo estarán disponibles solo para las clases pertenecientes al mismo paquete.

        "Private" Las clases o atributos con este acceso no estarán disponibles para ninguna otra clases, sus atributos solo pueden ser
         usados dentro de la misma clase y si queremos acceder a un atributos privado desde otra clase tendremos que hacerlo mediante 
         setter and getter.
    """

    ejemplo = """
        Un ejemplo del encapsulamiento para que se pueda entender mejor sería: En una desarrolladora de videojuegos por ejemplo 
        tenemos varíos departamentos pero tomaremos dos, por ejemplo los departamentos de arte, producción y diseño estos tres 
        tendrían acceso protected ya que se comunicarían entre sí pero no pueden comunicar los avances con otros departamentos 
        para evitar filtracciones, otro ejemplo por la misma linea sería, el equipo de producción tendría su acceso restringuido 
        cualquier otro y solo realizarían reportes a su jefe mediante informes o reuniones (acceso "Private" con getter and setter)
        
    """
    return concepto + explicacionTipos + ejemplo

print(Encapsulamiento())

Encapsulamiento_en_C_Sharp = """
    public class Empleado
    {
        private string Nombre { get; set; }
        private string Cedúla { get; set; }
        private int Edad { get; set; }
        private string puesto { get; set; }
        private string salario { get; set; }

        public Empleado(string nombre, string cedúla, int edad, string puesto, string salario) 
        {
            this.Nombre = nombre;
            this.Cedúla = cedúla;
            this.Edad = edad;
            this.puesto = puesto;
            this.salario = salario;
        }
    }
"""
Explicación = """
    En el ejemplo anterior desarrollado en C# tenemos una clase pública donde sus atributos tienen acceso privado lo que quiero decir que 
    solo se puede acceder a estos mediante getter and setter, también contiene un constructor público este debe ser público ya que
    debe ser asequible desde cualquier lugar del proyecto.
"""

print(Encapsulamiento_en_C_Sharp + Explicación)




def Herencia():

    concepto = """

        La herencia es un termino muy sencillo de entender, la herencia al igual que en la vida cotidiana en POO es cuando un hijo hereda
        cosas de su padre, pero en este caso es cuando una clase hija hereda los metodos y atributos de la clase padre o super clase. 

        Esto nos permite crear clases más complejas apartir de la super clase y tener una mayor reutilización de código. Cuando una clase 
        hereda a otra esta obtiene todos sus atributos y metodos.
        
    """

    ejemplo = """

        Un ejemplo de la herencia: Tenemos una clase Vehículo, dentro de esta clase tenemos los atributos y metodos generales relacionados
        con los vehículos, de esta clase podemos mediante la herencia crear varias clases más especificas como "Coche", "Moto", "Avión" 
        entre otras, estas clases hijas pueden incluir sus propios metodos y atributos.
    
    """

    
def Polimorfismo():

    concepto = """

        El polimorfismo es la manera que tenemos de que los metodos de una clase hija tenga sus propias funciones modificando o sobreescribiendo 
        los metodos de la clase padre o super clase. Esto nos permite que un solo metodos pueda tener varias funciones.
    """



    
    



