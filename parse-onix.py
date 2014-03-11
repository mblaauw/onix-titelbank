__author__ = 'mich'
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

onxFile = 'data/TB30_totaal_2014-03_073van073.onx'
soup = BeautifulSoup(open(onxFile, 'r'), features='lxml')

# collect unique ID's
productBlock = soup.find_all('product')
for eachProductBlock in productBlock:
    idValue.append(eachProductBlock.idvalue.string)
    idType.append(eachProductBlock.productidtype.string)

    # collect publishing details
    publishingSoup = BeautifulSoup(str(eachProductBlock), features='lxml')
    publishingBlock = publishingSoup.find_all('publishingdate')
    for eachPublishBlock in publishingBlock:
        publishingRole.append(eachPublishBlock.publishingdaterole.string)
        publishingDateFormat.append(eachPublishBlock.dateformat.string)
        publishingDate.append(eachPublishBlock.date.string)

    # collect descriptive details
    descriptiveSoup = BeautifulSoup(str(eachProductBlock), features='lxml')
    descriptiveBlock = descriptiveSoup.find_all('descriptivedetail')
    for eachDescriptiveBlock in descriptiveBlock:
        productComposition.append(eachDescriptiveBlock.productcomposition.string)
        productForm.append(eachDescriptiveBlock.productform.string)

        chkEditionNumber = descriptiveSoup.find_all('editionnumber')
        chkEditionStatement = descriptiveSoup.find_all('editionstatement')
        if len(chkEditionNumber) != 0:
            editionNumber.append(eachDescriptiveBlock.editionnumber.string)
        else:
            editionNumber.append('')
        if len(chkEditionStatement) != 0:
            editionStatement.append(eachDescriptiveBlock.editionstatement.string)
        else:
            editionStatement.append('')

        illustratedType.append(eachDescriptiveBlock.illustrated.string)
        languageRole.append(eachDescriptiveBlock.languagerole.string)
        languageCode.append(eachDescriptiveBlock.languagecode.string)
        subjectSchemeIdentifier.append(eachDescriptiveBlock.subjectschemeidentifier.string)
        subjectCode.append(eachDescriptiveBlock.subjectcode.string)

        # collect extent details
        extentSoup = BeautifulSoup(str(eachDescriptiveBlock), features='lxml')
        extentBlock = extentSoup.find_all('extent')
        if len(extentBlock) != 0:
            for eachExtentBlock in extentBlock:

                chkExtentType = eachExtentBlock.find_all('extenttype')
                if len(chkExtentType) != 0 and eachExtentBlock.extenttype.string == '00':
                    extentType.append(eachExtentBlock.extenttype.string)
                else:
                    extentType.append('')

                chkExtentValue = eachExtentBlock.find_all('extentvalue')
                if len(chkExtentValue) != 0 and eachExtentBlock.extenttype.string == '00':
                    extentValue.append(eachExtentBlock.extentvalue.string)
                else:
                    extentValue.append('')

                chkExtentUnit = eachExtentBlock.find_all('extentunit')
                if len(chkExtentUnit) != 0 and eachExtentBlock.extenttype.string == '00':
                    extentUnit.append(eachExtentBlock.extentunit.string)
                else:
                    extentUnit.append('')


result = zip(idValue, idType, publishingRole, publishingDateFormat,publishingDate,productComposition, productForm, editionStatement, editionNumber, illustratedType, languageRole, languageCode, subjectSchemeIdentifier, subjectCode, extentType, extentUnit, extentValue)

