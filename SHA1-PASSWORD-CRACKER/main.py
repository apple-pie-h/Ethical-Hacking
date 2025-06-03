import hashlib



def convert_txt_to_sha1(text):
    digest = hashlib.sha1(
        text.encode()
    ).hexdigest()
    return digest 

def main():
    usr_sha1= input("Enter the SHA1 to Crack: ")
    cleaned_usr_sha1= usr_sha1.strip().lower() #.strip remove leading and trailing white spaces
    
    with open('./passwords.txt') as f:
        for line in f:
            pwd=line.strip()
            converted_sha1 = convert_txt_to_sha1(pwd)
            
            if cleaned_usr_sha1 == converted_sha1:
                print (f"Password Found: {pwd}")
                return 
        
    print ("Could not find password")     
            
 
if __name__ =='__main__':
    main()
