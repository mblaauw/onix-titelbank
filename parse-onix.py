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
        # collect id details
        chkIdValue = eachProductBlock.find_all('RecordReference')
        chkIdType = eachProductBlock.find_all('NotificationType')
        if len(chkIdValue) != 0:
            idValue.append(chkIdValue[0].string)
        else:
            idValue.append('')

        if len(chkIdType) != 0:
            idType.append(chkIdType[0].string)
        else:
            idType.append('')

        # collect publishing details
        chkPublishingRole = eachProductBlock.find_all('PublishingRole')
        chkPublishingDateFormat = eachProductBlock.find_all('PublishingDateFormat')
        chkPublishingDate = eachProductBlock.find_all('PublishingDateFormat')
        if len(chkPublishingRole) != 0:
            publishingRole.append(chkPublishingRole[0].string)
        else:
            publishingRole.append('')

        if len(chkPublishingDateFormat) != 0:
            publishingDateFormat.append(chkPublishingDateFormat[0].string)
        else:
            publishingDateFormat.append('')

        if len(chkPublishingDate) != 0:
            publishingDate.append(chkPublishingDate[0].string)
        else:
            publishingDate.append('')


        # collect descriptive details
        descriptiveSoup = BeautifulSoup(str(eachProductBlock), features='xml')
        descriptiveBlock = descriptiveSoup.find_all('DescriptiveDetail')
        for eachDescriptiveBlock in descriptiveBlock:
            chkProductComposition = eachDescriptiveBlock.find_all('ProductComposition')
            chkProductForm = eachDescriptiveBlock.find_all('ProductForm')
            chkEditionNumber = eachDescriptiveBlock.find_all('EditionNumber')
            chkEditionStatement = eachDescriptiveBlock.find_all('EditionStatement')
            chkIllustratedType = eachDescriptiveBlock.find_all('Illustrated')
            chkLanguageRole = eachDescriptiveBlock.find_all('LanguageRole')
            chkLanguageCode = eachDescriptiveBlock.find_all('LanguageCode')
            chkSubjectSchemeIdentifier = eachDescriptiveBlock.find_all('SubjectSchemeIdentifier')
            chkSubjectCode = eachDescriptiveBlock.find_all('SubjectCode')

            if len(chkProductComposition) != 0:
                productComposition.append(chkProductComposition[0].string)
            else:
                productComposition.append('')

            if len(chkProductForm) != 0:
                productForm.append(chkProductForm[0].string)
            else:
                productForm.append('')

            if len(chkEditionNumber) != 0:
                editionNumber.append(chkEditionNumber[0].string)
            else:
                editionNumber.append('')

            if len(chkEditionStatement) != 0:
                editionStatement.append(chkEditionStatement[0].string)
            else:
                editionStatement.append('')

            if len(chkIllustratedType) != 0:
                illustratedType.append(chkIllustratedType[0].string)
            else:
                illustratedType.append('')

            if len(chkLanguageRole) != 0:
                languageRole.append(chkLanguageRole[0].string)
            else:
                languageRole.append('')

            if len(chkLanguageCode) != 0:
                languageCode.append(chkLanguageCode[0].string)
            else:
                languageCode.append('')

            if len(chkSubjectSchemeIdentifier) != 0:
                subjectSchemeIdentifier.append(chkSubjectSchemeIdentifier[0].string)
            else:
                subjectSchemeIdentifier.append('')

            if len(chkSubjectCode) != 0:
                subjectCode.append(chkSubjectCode[0].string)
            else:
                subjectCode.append('')

            # collect extent details
            extentSoup = BeautifulSoup(str(eachDescriptiveBlock), features='xml')
            extentBlock = extentSoup.find_all('Extent')
            if len(extentBlock) != 0:
                for eachExtentBlock in extentBlock:

                    chkExtentType = eachExtentBlock.find_all('ExtentType')
                    chkExtentValue = eachExtentBlock.find_all('ExtentValue')
                    chkExtentUnit = eachExtentBlock.find_all('ExtentUnit')

                    if len(chkExtentType) != 0:
                        extentType.append(chkExtentType[0].string)
                    else:
                        extentType.append('')

                    if len(chkExtentValue) != 0:
                        extentValue.append(chkExtentValue[0].string)
                    else:
                        extentValue.append('')

                    if len(chkExtentUnit) != 0:
                        extentUnit.append(chkExtentUnit[0].string)
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


for i in range(2,73):
    if len(str(i)) == 1:
        fileNr = '00' + str(i)
    else:
        fileNr = '0' + str(i)


    onxFile = 'titelbank/TB30_totaal_2014-03_' + fileNr + 'van073.onx/TB30_totaal_2014-03_' + fileNr + 'van073.onx'

    result = parseOnxFiles(onxFile)
    store_results(result)




