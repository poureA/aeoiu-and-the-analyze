class Check(object):
    '''class docstring'''
    def __init__(self,text)->None:
        self.t = text
    def check(self)->None:
        '''function docstring'''
        alpha = [chr(i) for i in range(ord('a'),ord('z')+1)]
        ALPHA = [chr(i) for i in range(ord('A'),ord('Z')+1)]
        alpha.append(' ')
        ALPHA.append(' ')
        a = 0
        e = 0
        o = 0
        i_ = 0
        u = 0
        for i in self.t :
            if i not in alpha :
                if i not in ALPHA :
                    print('error')
                    return
        for i in self.t :
            if i == 'a' or i == 'A' :
                a+=1
            if i == 'e' or i == 'E' :
                e+=1
            if i == 'o' or i == 'O' :
                o+=1
            if i == 'i' or i == 'I' :
                i_+=1
            if i == 'u' or i == 'U' :
                u+=1
        aeoiu = [a,e,o,i_,u]
        aeoiu_str = ['a','e','o','i','u']
        text_list = self.t.split()
        the = 0
        for i in text_list :
            if i[0]=='t' or i[0]=='T' :
                if i[1]=='h' or i[1]=='H' :
                    if i[2]=='e' or i[2]=='E' :
                        the+=1
        print(f'there are {the} "the" in the text')
        c = 0
        for i in aeoiu :
            star = '*'*i
            print(f'{aeoiu_str[c]} {star}')
            c+=1
        return
sample = Check(input('enter a text here :'))
sample.check()
exit = input('enter any key to exit :')
