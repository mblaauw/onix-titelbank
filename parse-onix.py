__author__ = 'mich'
import numpy as np
import sqlite3
from bs4 import BeautifulSoup

idValue = list()
idType = list()
publishingRole = list()
publishingDateFormat = list()
publishingDate = list()
productComposition = list()
productForm = list()
editionStatement = list()
editionNumber  = list()
illustratedType  = list()
languageRole = list()
languageCode = list()
subjectSchemeIdentifier = list()
subjectCode = list()
extentType = list()
extentUnit = list()
extentValue = list()


def parseOnxFiles(onxFile):
    print onxFile
    soup = BeautifulSoup(open(onxFile, 'r'), features='xml')

    # collect unique ID's
    productBlock = soup.find_all('Product')
    print 'books to process: ' + str(len(productBlock))

    for eachProductBlock in productBlock:

        chkIdValue = eachProductBlock.find_all('IDValue')
        print chkIdValue
        if len(chkIdValue) != 0:
            idValue.append(eachProductBlock.idvalue.string)
        else:
            idValue.append('')

        chkIdType = eachProductBlock.find_all('IDType')
        if len(chkIdValue) != 0:

            idType.append(eachProductBlock.productidtype.string)
        else:
            idType.append('')


        # collect publishing details
        publishingSoup = BeautifulSoup(str(eachProductBlock), features='xml')
        publishingBlock = publishingSoup.find_all('PublishingDate')
        for eachPublishBlock in publishingBlock:
            publishingRole.append(eachPublishBlock.publishingdaterole.string)
            publishingDateFormat.append(eachPublishBlock.dateformat.string)
            publishingDate.append(eachPublishBlock.date.string)

        # collect descriptive details
        descriptiveSoup = BeautifulSoup(str(eachProductBlock), features='xml')
        descriptiveBlock = descriptiveSoup.find_all('DescriptiveDetail')
        for eachDescriptiveBlock in descriptiveBlock:
            chkProductComposition = descriptiveSoup.find_all('ProductComposition')
            chkProductForm = descriptiveSoup.find_all('ProductForm')
            chkEditionNumber = descriptiveSoup.find_all('EditionNumber')
            chkEditionStatement = descriptiveSoup.find_all('EditionStatement')
            chkIllustratedType = descriptiveSoup.find_all('Illustrated')
            chkLanguageRole = descriptiveSoup.find_all('LanguageRole')
            chkLanguageCode = descriptiveSoup.find_all('LanguageCode')
            chkSubjectSchemeIdentifier = descriptiveSoup.find_all('SubjectSchemeIdentifier')
            chkSubjectCode = descriptiveSoup.find_all('SubjectCode')

            if len(chkProductComposition) != 0:
                productComposition.append(eachDescriptiveBlock.productcomposition.string)
            else:
                productComposition.append('')

            if len(chkProductForm) != 0:
                productForm.append(eachDescriptiveBlock.productform.string)
            else:
                productForm.append('')

            if len(chkEditionNumber) != 0:
                editionNumber.append(eachDescriptiveBlock.editionnumber.string)
            else:
                editionNumber.append('')

            if len(chkEditionStatement) != 0:
                editionStatement.append(eachDescriptiveBlock.editionstatement.string)
            else:
                editionStatement.append('')

            if len(chkIllustratedType) != 0:
                illustratedType.append(eachDescriptiveBlock.illustrated.string)
            else:
                illustratedType.append('')

            if len(chkIllustratedType) != 0:
                languageRole.append(eachDescriptiveBlock.languagerole.string)
            else:
                languageRole.append('')

            if len(chkIllustratedType) != 0:
                languageCode.append(eachDescriptiveBlock.languagecode.string)
            else:
                languageCode.append('')

            if len(chkSubjectSchemeIdentifier) != 0:
                subjectSchemeIdentifier.append(eachDescriptiveBlock.subjectschemeidentifier.string)
            else:
                subjectSchemeIdentifier.append('')

            if len(chkSubjectCode) != 0:
                subjectCode.append(eachDescriptiveBlock.subjectcode.string)
            else:
                subjectCode.append('')

            # collect extent details
            extentSoup = BeautifulSoup(str(eachDescriptiveBlock), features='xml')
            extentBlock = extentSoup.find_all('Extent')
            if len(extentBlock) != 0:
                for eachExtentBlock in extentBlock:

                    chkExtentType = eachExtentBlock.find_all('ExtentType')
                    if len(chkExtentType) != 0 and eachExtentBlock.extenttype.string == '00':
                        extentType.append(eachExtentBlock.extenttype.string)
                    else:
                        extentType.append('')

                    chkExtentValue = eachExtentBlock.find_all('ExtentValue')
                    if len(chkExtentValue) != 0 and eachExtentBlock.extenttype.string == '00':
                        extentValue.append(eachExtentBlock.extentvalue.string)
                    else:
                        extentValue.append('')

                    chkExtentUnit = eachExtentBlock.find_all('ExtentUnit')
                    if len(chkExtentUnit) != 0 and eachExtentBlock.extenttype.string == '00':
                        extentUnit.append(eachExtentBlock.extentunit.string)
                    else:
                        extentUnit.append('')


    result = np.array(zip(idValue, idType, publishingRole, publishingDateFormat,publishingDate,productComposition, productForm, editionStatement, editionNumber, illustratedType, languageRole, languageCode, subjectSchemeIdentifier, subjectCode, extentType, extentUnit, extentValue))

    return result


def store_results(npArray, dbName = 'sample.db'):
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    cursor.executemany('''insert into data values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', map(tuple, npArray.tolist()))
    conn.commit()
    cursor.close()
    conn.close()


def create_initial_db(dbName = 'sample.db'):
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    cursor.execute('''create table data (
        idValue NVARCHAR(13),
        idType NVARCHAR(5),
        publishingRole NVARCHAR(5),
        publishingDateFormat NVARCHAR(5),
        publishingDate NVARCHAR(8),
        productComposition NVARCHAR(5),
        productForm NVARCHAR(5),
        editionStatement NVARCHAR(15),
        editionNumber NVARCHAR(5),
        illustratedType NVARCHAR(5),
        languageRole NVARCHAR(5),
        languageCode NVARCHAR(5),
        subjectSchemeIdentifier NVARCHAR(5),
        subjectCode NVARCHAR(5),
        extentType NVARCHAR(5),
        extentUnit NVARCHAR(5),
        extentValue  NVARCHAR(5)
    )''')

    conn.commit()
    cursor.close()
    conn.close()




for i in range(20,22):
    if len(str(i)) == 1:
        fileNr = '00' + str(i)
    else:
        fileNr = '0' + str(i)


    onxFile = 'titelbank/TB30_totaal_2014-03_' + fileNr + 'van073.onx/TB30_totaal_2014-03_' + fileNr + 'van073.onx'

    result = parseOnxFiles(onxFile)
    store_results(result)




