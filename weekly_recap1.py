# LIST RECAP

pastor = 'Pastor Ramathe'
first_lady = 'Mme Ramathe'
drummer = 'Mohale'
keyboardist = 'Ntate Tshepo'
worship_team = ['Hloni', 'Mme Mamohale','Mme Nhlapho', 'Sister Busi', 'Sister Mpho']
media = ['Tankiso', 'Precious', 'Mr Thabo Mzima']
ushers = ['Mme Mzima', 'Mme Selepe', 'Sister Nnana']
congregation = 54

church = [pastor, first_lady, drummer, keyboardist, worship_team, media, congregation]

print(church)

print(type(church))

music = list(church)

music_team = music[2 : -2]

# music = church[:]
print('music team consists of ', music_team)

del media[2] 

media_team = media + ['Mr S Mzima']

print(media_team)