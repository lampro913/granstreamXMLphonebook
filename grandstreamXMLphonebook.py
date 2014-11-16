#! /usr/bin/python3

import sys
import csv
from string import Template

def main(argv):
    if len(argv) == 2:
        csvLocation, xmlOutFile = argv
    else:
        print('Not enough arguments!')
        sys.exit()
        
    #create dictionary object out of csv file
    xmlString = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<AddressBook>\n"
    f = open(csvLocation, 'r')
    csvDict = csv.DictReader(f, delimiter=',', quotechar='"')
    
    #loop through contact rows, extract unique list of groups for initial group decelration
    gp = []
    for row in csvDict:
        #split groups
        b = row['Group Membership'].split(" ::: ")
        #cleanup groups list
        gp += [x.strip().replace('* ','') for x in b if x != "* My Contacts"]
        #remove leading '* '
    #make ending list unique
    gp = list(set(gp))
    
    #create xml groups
    groupTemplate = Template('\t<pbgroup>\n\t\t<id>${id}</id>\n\t\t<name>${gname}</name>\n\t</pbgroup>\n')
    groupIndexTable = []
    idIndx = 0
    for g in gp:
        xmlString += groupTemplate.substitute(id=idIndx, gname=g)
        groupIndexTable.append(g)
        idIndx += 1
    
    #create templates for contacts
    contactTemplate = Template('\t<Contact>\n\t\t<FirstName>${t_first}</FirstName>\n\t\t<LastName>${t_last}</LastName>\n\t\t<Frequent>0</Frequent>\n\t\t<Department>${t_dept}</Department>\n')
    phoneTemplate = Template('\t\t<Phone type="${t_pType}">\n\t\t\t<phonenumber>${t_pnumber}</phonenumber>\n\t\t\t<accountindex>0</accountindex>\n\t\t</Phone>\n')
    contactGroupTemplate = Template('\t\t<Group>${t_gp}</Group>\n')
    
    #reset iterable csvDict object and iterate again
    f.seek(0)
    csvDict.__init__(f, delimiter=",", quotechar='"')
    for row in csvDict:
        if len(row['Name']) > 0:
            first, *last = row['Name'].split()
            last = " ".join(last)
            xmlString += contactTemplate.substitute(t_first=first, t_last=last, t_dept='')
            
            #now loop through phone records and create nested dicts for each number
            a = {}
            pData = {k:v for k, v in row.items() if k.startswith('Phone')}
            for key, val in pData.items():
                _, num, _, TorV = key.split()
                if val != '':
                    if not ('Phone ' + str(num)) in a.keys():
                        a['Phone ' + str(num)] = {}
                    if TorV == "Type":
                        a['Phone ' + str(num)]['Type'] = val
                    if TorV == "Value":
                        #split multiple numbers of same type into list
                        a['Phone ' + str(num)]['Number'] = val.split(' ::: ')
                           
            #add values from nested dicts to xmlString
            for _, vals in a.items():
                for subNum in vals['Number']:            
                    xmlString += phoneTemplate.substitute(t_pType=vals['Type'], t_pnumber=subNum)
        
            #contact groups (add user to group(s))
            g = []
            if ' ::: ' in row['Group Membership']:
                cGroups = row['Group Membership'].split(' ::: ')
                g += [x.strip().replace('* ','') for x in cGroups if x != "* My Contacts"]
                for cg in g:
                    #lookup group name to get index
                    indx = groupIndexTable.index(cg)
                    xmlString += contactGroupTemplate.substitute(t_gp=indx)
        
            #end contact
            xmlString += '\t</Contact>\n'
    xmlString += '</AddressBook>'
                
    #create xml file
    with open(xmlOutFile, "w") as f:
        f.write(xmlString)
        f.close()
        
if __name__ == '__main__':
    main(sys.argv[1:])
