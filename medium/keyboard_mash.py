# flag = something

stuff = list(flag[12:-1])

ciphertext = ""
parity = 1

while len(stuff) != 0:
    val = stuff.pop(0)

    if parity % 2 == 0:
        ciphertext += int(valval) * val
        parity += 1
        continue
    
    print("".join(stuff))
    valval = val
    parity += 1

# ciphertext = ZccAAJeHHDvvaa88dwwMMoo)SShhLLrrQZZBBL&==99FFK)44$$cCC66PPvvbgg2hWWHHpp588SStaaFF!J<<4IImZRhhRRuH?xxNaMc..644pp9==wwKuu44VHH,,@@LL;;y$bb688nppAAddTTXXzzkXX77USS(uDDaaTGF-<<dB*::=i::Fdkk77-RREEVeeucc;;EE))33-ff22BBtyyf==44EE>hhzzMee%%G,,yy+GGaE66JQZZ5$$5nnp11$00.lluuk99g5n**HHgbb.yuu$$b8CffdMQQM.hh0077@@bb2<mkkTTBBddWWJJj3-11IIKBBKKoovvOaaAMMQQ#3>>3LDZZ;;mm11ffssRRLLwyyZ##ppWXXf1--JJEEllUU99))WWRR11TseL&RVVVw==ww?@aa44NzzSNccjPqqKKtt))??PP(&&AAm99b88<o5nnTm66Y44FFF==9%KKjD$jjGGyqqQQIIwwKKd,bbLLDD95RR==VVUdjj!!kWyb@@nfAYn:JFTtt,,bbvv=>VQQVcCC8B;;zz88>>WYuu+hhZZ((ddBB>>vvzzr22ZZ2277II==YY-44o&ooBGDDoCC)).rrAA??Zaa))2f+SSRdd(iiee--&&H3MD844dd7b00rrIIPP::AAVVbE77HHllgPttvmnffyH$$2200VVggttXcc122@3:WyyvJjbNN))K;IIxVVIIA**99jjA33;445QQff>>#YYNNFFttVEEUU77
