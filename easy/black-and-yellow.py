# flag = something

# this grabs whatever is inside CTFInfocomm{...}
stuff_inside_braces = flag[12:-1]

ciphertext = ""

for word in stuff_inside_braces.split():
    altered = word[1:] + word[0]

    ciphertext += altered + "ay "

# ciphertext = ccordingaay otay llaay nownkay awslay foay viationaay heretay siay onay ayway aay eebay houldsay ebay bleaay otay lyfay tsIay ingsway reaay ootay mallsay otay etgay tsiay atfay ittlelay odybay ffoay hetay roundThegay eebay foay oursecay liesfay nywayaay ecausebay eesbay ontday arecay hatway umanshay hinktay siay mpossibleiay
