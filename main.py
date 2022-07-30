import quad_eq
import nth_terms

def mainloop():
    func = input('Select your function (nth terms [nth], generate sequences from nth term formulas [gnth]): ')

    if func.lower() == 'nth terms'.lower() or func.lower() == 'nth'.lower():
        nth_terms.nth_terms()
    elif func.lower() == 'generate sequences from nth term formulas'.lower() or func.lower() == 'gnth'.lower():
        nth_terms.generate_sequence()

    input()
    mainloop()
    
mainloop()