import physics

physics.greet()

#print(physics.ZADANI_PRVE)
#physics.Vypocet(physics.ZADANI_PRVE)

#print(physics.ZADANI_DRUHE)
#physics.Vypocet(physics.ZADANI_DRUHE)

#print(physics.ZADANI_TRETI)
#physics.Vypocet(physics.ZADANI_TRETI)

prvni_priklad = {
    "zadani": physics.ZADANI_PRVE,
    "cislo": 1,
    "X": {"name": "s", "value": 0, "unit": "m"},
    "Y": {"name": "t", "value": 1.5, "unit": "s"},
    "Z": {"name": "v", "value": physics.SPEED_OF_SOUND, "unit": "m/s"}
}
physics.Vypocet(prvni_priklad['zadani'], prvni_priklad['cislo'], prvni_priklad['X'], prvni_priklad['Y'], prvni_priklad['Z'])


druhy_priklad = {
    "zadani": physics.ZADANI_DRUHE,
    "cislo": 2,
    "X": {"name": "f", "value": 0, "unit": "Hz"},
    "Y": {"name": "Lambda", "value": 590, "unit": "m"},
    "Z": {"name": "v", "value": physics.SPEED_OF_LIGHT, "unit": "m/s"}
}
physics.Vypocet(druhy_priklad['zadani'], druhy_priklad['cislo'], druhy_priklad['X'], druhy_priklad['Y'], druhy_priklad['Z'])


treti_priklad = {
    "zadani": physics.ZADANI_TRETI,
    "cislo": 3,
    "X": {"name": "m", "value": 0, "unit": "kg"},
    "Y": {"name": "Rz", "value": 6.378e6, "unit": "m"},
    "Z": {"name": "Rm", "value": 1.72e6, "unit": "m"}
}
physics.Vypocet(treti_priklad['zadani'], treti_priklad['cislo'], treti_priklad['X'], treti_priklad['Y'], treti_priklad['Z'])