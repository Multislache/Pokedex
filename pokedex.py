import tkinter as tk
import Pokemon as pk


###############################################################################
#                                  LOGIQUE                                    #
###############################################################################

###############################################
# Affichage des caractéristiques d'un pokemon #
###############################################
langue = 'eng'
liste_pokemons = pk.Pokemon.table_name()                              # Pokemon
nombre_de_pokemons = pk.Pokemon.effectif()  
liste_pokemons2 = pk.Pokemon.table_nom()
nombre_de_pokemons2 = pk.Pokemon.effectif2() 


def affiche_pokemon(poke: pk.Pokemon):                                # Pokemon
    """Affiche les caractéristique d'un pokemon."""
    global image_type2_file, image_type1_file, image_type1, image_type2,\
        image_dos, image_dos_pokemon, image_face, image_face_pokemon,\
        image_art, image_art_pokemon

    # Récupération des attributs
    if poke is not None:
        label_attribut_nom['text'] = poke.get_nom()                   # Pokemon
        label_attribut_nom_anglais['text'] = poke.get_name()          # Pokemon
        label_attribut_pv['text'] = poke.get_pv()                     # Pokemon
        label_attribut_attaque['text'] = poke.get_attaque()           # Pokemon
        label_attribut_defense['text'] = poke.get_defense()           # Pokemon
        label_attribut_attaque_speciale['text'] = poke.get_attaque_speciale()
                                                                      # Pokemon
        label_attribut_defense_speciale['text'] = poke.get_defense_speciale()
                                                                      # Pokemon
        label_attribut_vitesse['text'] = poke.get_vitesse()
                                                                      # Pokemon
        try:
            label_attribut_evolution['text'] = poke.ascendant().get_name()
                                                                      # Pokemon
        except:
            label_attribut_evolution['text'] = "..."
        label_zone_description['text'] = poke.get_description()
                                                                      # Pokemon

        # Recherche des images stockées l'attribut id_img
        try:
            chemin_image_face = "img_front/"+str(poke.get_id_img())+".png"
                                                                      # Pokemon
            image_face = tk.PhotoImage(file=chemin_image_face)
            monCanvas.itemconfig(image_face_pokemon, image=image_face)
        except:
            chemin_image_face = "img/fond_pokemon.png"
            image_face = tk.PhotoImage(file=chemin_image_face)
            monCanvas.itemconfig(image_face_pokemon, image=image_face)
        try:
            chemin_image_dos = "img_back/"+str(poke.get_id_img())+".png"
                                                                      # Pokemon
            image_dos = tk.PhotoImage(file=chemin_image_dos)
            monCanvas.itemconfig(image_dos_pokemon, image=image_dos)
        except:
            chemin_image_face = "img/fond_pokemon.png"
            image_face = tk.PhotoImage(file=chemin_image_face)
            monCanvas.itemconfig(image_face_pokemon, image=image_face)
        try:
            chemin_image_dos = "img_art/"+str(poke.get_id_img())+".png"
                                                                      # Pokemon
            image_art = tk.PhotoImage(file=chemin_image_dos)
            monCanvas.itemconfig(image_art_pokemon, image=image_art)
        except:
            chemin_image_art = "img/fond_art_pokemon.png"
            image_art = tk.PhotoImage(file=chemin_image_art)
            monCanvas.itemconfig(image_art_pokemon, image=image_art)

        # Recherche des types
        liste = poke.types()                                          # Pokemon
        chemin_image_type = "img/fond_type.png"
        image_type1_file = tk.PhotoImage(file=chemin_image_type)
        image_type2_file = tk.PhotoImage(file=chemin_image_type)
        monCanvas.itemconfig(image_type1, image=image_type1_file)
        monCanvas.itemconfig(image_type2, image=image_type2_file)
        # Si la liste contient un seul type
        if len(liste) == 1:
            chemin_image_type1 = f"img_types/{liste[0]}.png"
            image_type1_file = tk.PhotoImage(file=chemin_image_type1)
            monCanvas.itemconfig(image_type1, image=image_type1_file)
        # Si la liste contient 2 types
        elif len(liste) == 2:
            chemin_image_type1 = f"img_types/{liste[0]}.png"
            image_type1_file = tk.PhotoImage(file=chemin_image_type1)
            monCanvas.itemconfig(image_type1, image=image_type1_file)
            chemin_image_type2 = f"img_types/{liste[1]}.png"
            image_type2_file = tk.PhotoImage(file=chemin_image_type2)
            monCanvas.itemconfig(image_type2, image=image_type2_file)




###############################################################################
#                                   VUE                                       #
###############################################################################


######################
# Fenêtre principale #
######################
fenetre = tk.Tk()
fenetre.geometry("1155x800")
fenetre.title("POKEDEX")
fenetre.resizable(False, False)
monCanvas = tk.Canvas(fenetre, width=1150, height=800)
monCanvas.place(x=0, y=0)
monFond = tk.PhotoImage(file="img/fondred.png")
monCanvas.create_image(0, 0, image=monFond, anchor="nw")

######################
# Liste des pokemons #
######################
maListeBox = tk.Listbox(fenetre, width=30, height=8, borderwidth=0,
                        selectborderwidth=0, selectmode='single',
                        highlightthickness=0, font=('arial', '16'))

maListeBox2 = tk.Listbox(fenetre, width=30, height=8, borderwidth=0,
                        selectborderwidth=0, selectmode='single',
                        highlightthickness=0, font=('arial', '16'))

maListeBox.place(x=44, y=217)
if langue =='eng':
    if liste_pokemons is not None:
        for nom in liste_pokemons:
            maListeBox.insert('end',nom)
    maListeBox_flag = True
else:
    if liste_pokemons2 is not None:
        for nom in liste_pokemons2:
            maListeBox.insert('end',nom)
    maListeBox_flag = True
    


#############################
# Liste de caractéristiques #
#############################
image_face = tk.PhotoImage(file="img/fond_pokemon.png")
image_dos = tk.PhotoImage(file="img/fond_pokemon.png")
image_face_pokemon = monCanvas.create_image(640, 50, image=image_face,
                                            anchor="nw")
image_dos_pokemon = monCanvas.create_image(800, 50, image=image_dos,
                                           anchor="nw")
image_art = tk.PhotoImage(file="img/fond_art_pokemon.png")
image_art_pokemon = monCanvas.create_image(830, 540, image=image_art,
                                           anchor="nw")
image_type1_file = tk.PhotoImage(file="img/fond_type.png")
image_type2_file = tk.PhotoImage(file="img/fond_type.png")
image_type1 = monCanvas.create_image(1000, 70, image=image_type1_file,
                                     anchor="nw")
image_type2 = monCanvas.create_image(1000, 100, image=image_type2_file,
                                     anchor="nw")
label_nom = tk.Label(fenetre, text="Nom:", foreground="black",
                     background="white", font=('arial', '16'))
label_nom.place(x=640, y=150)
label_nom_anglais = tk.Label(fenetre, text="Nom anglais:", foreground="black",
                             background="white", font=('arial', '16'))
label_nom_anglais.place(x=640, y=180)
label_pv = tk.Label(fenetre, text="PV:", foreground="black",
                    background="white", font=('arial', '16'))
label_pv.place(x=640, y=210)
label_attaque = tk.Label(fenetre, text="Attaque:", foreground="black",
                         background="white", font=('arial', '16'))
label_attaque.place(x=640, y=240)
label_defense = tk.Label(fenetre, text="Défense:", foreground="black",
                         background="white", font=('arial', '16'))
label_defense.place(x=640, y=270)
label_attaque_speciale = tk.Label(fenetre, text="Attaque spéciale:",
                                  foreground="black", background="white",
                                  font=('arial', '16'))
label_attaque_speciale.place(x=640, y=300)
label_defense_speciale = tk.Label(fenetre, text="Défense spéciale:",
                                  foreground="black", background="white"
                                  , font=('arial', '16'))
label_defense_speciale.place(x=640, y=330)
label_vitesse = tk.Label(fenetre, text="Vitesse:", foreground="black",
                         background="white", font=('arial', '16'))
label_vitesse.place(x=640, y=360)
label_evolution = tk.Label(fenetre, text="Evolution de:", foreground="black",
                           background="white", font=('arial', '16'))
label_evolution.place(x=640, y=390)
label_description = tk.Label(fenetre, text="Description:",
                             foreground="black", background="white"
                             , font=('arial', '16'))
label_description.place(x=640, y=420)
label_zone_description = tk.Label(fenetre, text='...', foreground="black",
                                  width=35, height=4, background="white",
                                  borderwidth=0, font=('arial', '14'))
label_zone_description.place(x=660, y=460)
label_attribut_nom = tk.Label(fenetre, text="...", foreground="black",
                              background="white", font=('arial', '16'))
label_attribut_nom.place(x=900, y=150)
label_attribut_nom_anglais = tk.Label(fenetre, text="...", foreground="black",
                                      background="white", font=('arial', '16'))
label_attribut_nom_anglais.place(x=900, y=180)
label_attribut_pv = tk.Label(fenetre, text="...", foreground="black",
                             background="white", font=('arial', '16'))
label_attribut_pv.place(x=900, y=210)
label_attribut_attaque = tk.Label(fenetre, text="...", foreground="black",
                                  background="white", font=('arial', '16'))
label_attribut_attaque.place(x=900, y=240)
label_attribut_defense = tk.Label(fenetre, text="...", foreground="black",
                                  background="white", font=('arial', '16'))
label_attribut_defense.place(x=900, y=270)
label_attribut_attaque_speciale = tk.Label(fenetre, text="...",
                                           foreground="black",
                                           background="white",
                                           font=('arial', '16'))
label_attribut_attaque_speciale.place(x=900, y=300)
label_attribut_defense_speciale = tk.Label(fenetre, text="...",
                                           foreground="black",
                                           background="white",
                                           font=('arial', '16'))
label_attribut_defense_speciale.place(x=900, y=330)
label_attribut_vitesse = tk.Label(fenetre, text="...", foreground="black",
                                  background="white", font=('arial', '16'))
label_attribut_vitesse.place(x=900, y=360)
label_attribut_evolution = tk.Label(fenetre, text="...", foreground="black",
                                    background="white", font=('arial', '16'))
label_attribut_evolution.place(x=900, y=390)

###################
# Bouton Pokedex #
###################
boutonSelect = tk.Button(fenetre, text='Pokedex', width='12')
boutonSelect.place(x=60, y=470)


#######################
# Bouton Langue #
#######################
boutonLangue = tk.Button(fenetre, text='Langue', width='12')
boutonLangue.place(x=220, y=550)


#######################
# Bouton Evolution_de #
#######################
boutonEvoDe = tk.Button(fenetre, text='Evolution de', width='12')
boutonEvoDe.place(x=220, y=470)


####################
# Bouton Evolue_en #
####################
boutonEvoEn = tk.Button(fenetre, text='Evolue en', width='12')
boutonEvoEn.place(x=380, y=470)


################
# Bouton Start #
################
boutonStart = tk.Button(fenetre, text='Initilisation', font=('arial', '16'))
boutonStart.place(x=30, y=20)


#####################
# Recherche par nom #
#####################
recherche_txt = tk.Label(fenetre, text='Recherche par nom :')
recherche = tk.Entry(fenetre)
recherche_txt.place(x=50, y=600)
recherche.place(x = 180, y=600)


#####################
# Nombre de pokemon #
#####################

label_nbr_pokemons_texte = tk.Label(fenetre,
                                    text="Nombre de pokemons dans le pokedex",
                                    font=('arial', '16'))
label_nbr_pokemons_texte.place(x=40, y=690)

if langue == 'eng':
    label_nbr_pokemons = tk.Label(fenetre, text=nombre_de_pokemons, font=('arial',
                                                                      '16'))
elif langue == 'fra':
    label_nbr_pokemons = tk.Label(fenetre, text=nombre_de_pokemons2, font=('arial',
                                                                      '16'))
    
label_nbr_pokemons.place(x=220, y=715)


#####################
#      Langue       #
#####################




affichage_langue = tk.Label(fenetre,
                                    text="Le pokédex est en",
                                        font=('arial', '12'))
affichage_langue.place(x=300, y=150)

langue_de = tk.Label(fenetre, text=langue, font=('arial',
                                                                          '12'))
langue_de.place(x=434, y=150)




###############################################################################
#                                Contrôleur                                   #
###############################################################################

#############################
# Gestionnaires d'événement #
#############################

def boutonSelect_clic(event):
    """Déclenche l'affichage au clic sur le bouton select."""
    if langue =='eng':
        if maListeBox_flag is True:
            valeur = maListeBox.curselection()
            if valeur == ():
                print("rien n'a été sélectionné")
            else:
                poke_name = maListeBox.get(valeur[0])
                poke = pk.Pokemon(poke_name)                              # Pokemon
                affiche_pokemon(poke)
    elif langue =='fra':
        if maListeBox_flag is True:
            valeur = maListeBox.curselection()
            if valeur == ():
                print("rien n'a été sélectionné")
            else:
                poke_nom = maListeBox.get(valeur[0])
                poke = pk.Pokemon(poke_nom)                              # Pokemon
                affiche_pokemon(poke)
        
        


def boutonEvoDe_clic(event):
    """Déclenche l'affichage de l'ascendant du pokemon courant."""
    evolution_de = label_attribut_evolution["text"]
    if langue =='eng':
        if evolution_de != "...":
            affiche_pokemon(pk.Pokemon(evolution_de))                     # Pokemon
            maListeBox.delete(0, 'end')
            maListeBox.insert('end', evolution_de)
            maListeBox.selection_set(0)
    else:
        if langue == 'fra':
             if evolution_de != "...":
                affiche_pokemon(pk.Pokemon(evolution_de))                     # Pokemon
                maListeBox.delete(0, 'end')
                maListeBox.insert('end', evolution_de)
                maListeBox.selection_set(0)


def boutonEvoEn_clic(event):
    """Déclenche l'affichage des évolutions."""
    global maListeBox_flag
    nom_pokemon = label_attribut_nom_anglais["text"]
    print(nom_pokemon)
    if nom_pokemon != "...":
        poke = pk.Pokemon(nom_pokemon)                                # Pokemon
        liste_evolutions = poke.descendants()                         # Pokemon
        maListeBox.delete(0, 'end')
        if langue == 'eng':
            if liste_evolutions == []:
                maListeBox.insert('end', "Ce pokemon n'a pas d'évolution")
                maListeBox_flag = False
            else:
                for poke in liste_evolutions:
                    maListeBox.insert('end', poke.get_name())
                maListeBox_flag = True
        else:
            if liste_evolutions == []:
                maListeBox.insert('end', "Ce pokemon n'a pas d'évolution")
                maListeBox_flag = False
            else:
                for poke in liste_evolutions:
                    maListeBox.insert('end', poke.get_nom())
                maListeBox_flag = True
            
        



def boutonStart_clic(event):
    """Initialise l'affichage de la liste des pokemons."""
    global maListeBox_flag
    maListeBox.delete(0, 'end')
    if langue == 'eng':
        if liste_pokemons is not None:
            for nom in liste_pokemons:
                maListeBox.insert('end', nom)
            maListeBox_flag = True
    else:
        if liste_pokemons2 is not None:
            for nom in liste_pokemons2:
                maListeBox.insert('end', nom)
            maListeBox_flag = True
        
    


def boutonLangue_clic(event):
    """Change la langue d'affichage des noms."""
    global langue
    global langue_de
    if langue == 'fra':
        langue = 'eng'
        boutonStart_clic(event)
        langue_de = tk.Label(fenetre, text=langue, font=('arial',
                                                                          '12'))
        langue_de.place(x=434, y=150)
    else:
        langue = 'fra'
        boutonStart_clic(event)
        langue_de = tk.Label(fenetre, text=langue, font=('arial',
                                                                          '12'))
        langue_de.place(x=438, y=150)

def chercher_pokemon(event):
    """Déclenche la recherche d'un pokemon."""
    
    if langue =='eng':
        name = recherche.get()
        if name in pk.Pokemon.table_name():                               # Pokemon
            poke = pk.Pokemon(name)                                       # Pokemon
            affiche_pokemon(poke)
            maListeBox.delete(0, 'end')
            maListeBox.insert('end', poke.get_name())                     # Pokemon
            maListeBox.selection_set(0)
    elif langue =='fra':
        nom = recherche.get()
        if nom in pk.Pokemon.table_nom():                               # Pokemon
            poke = pk.Pokemon(name)                                       # Pokemon
            affiche_pokemon(poke)
            maListeBox.delete(0, 'end')
            maListeBox.insert('end', poke.get_nom())                     # Pokemon
            maListeBox.selection_set(0)
        


#############################
# Surveillance d'événements #
#############################
boutonSelect.bind('<Button-1>', boutonSelect_clic)
boutonLangue.bind('<Button-1>', boutonLangue_clic)
boutonStart.bind('<Button-1>', boutonStart_clic)
boutonEvoDe.bind('<Button-1>', boutonEvoDe_clic)
boutonEvoEn.bind('<Button-1>', boutonEvoEn_clic)
recherche.bind("<Return>", chercher_pokemon)
maListeBox.bind('<Double-Button-1>',boutonSelect_clic)


###############################################################################
#                                 LANCEMENT                                   #
###############################################################################
fenetre.mainloop()
fenetre.quit()