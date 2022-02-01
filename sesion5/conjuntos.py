frutas = {"manzanas","fresas","cerezas"}
#print(type(frutas))
#print(frutas)
#todo adicionar elementos al set
frutas.add("platanos")
#print(frutas)
#todo adicionar multiples elementos al set
frutas.update(["naranja","sandia","coco"])
#print(frutas)
#todo remover valores del set
frutas.remove("coco")
#print(frutas)
#todo tratar de modificar un valor del set
#todo no esta permitido
#frutas[0]="maracuya"
print(frutas)
#todo no permite elementos duplicados
frutas.add("platanos")