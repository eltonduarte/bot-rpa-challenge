from tasks.log import log_to_file

def preenche_formulario(bot, index, row, PATH_LOG):
       
        log_to_file(f"Round {index}", PATH_LOG)

        # Preenche o campo 'First Name' 
        bot.find_element('xpath', "//input[@ng-reflect-name = 'labelFirstName']").send_keys(row['First Name'])
        log_to_file("Campo 'First Name' preenchido com sucesso.", PATH_LOG)

        # Preenche o campo 'Last Name'
        bot.find_element('xpath', "//input[@ng-reflect-name = 'labelLastName']").send_keys(row['Last Name '])
        log_to_file("Campo 'Last Name' preenchido com sucesso.", PATH_LOG)

        # Preenche o campo 'Phone Number'
        bot.find_element('xpath', "//input[@ng-reflect-name = 'labelPhone']").send_keys(row['Phone Number'])
        log_to_file("Campo 'Phone Number' preenchido com sucesso.", PATH_LOG)

        # Preenche o campo 'Company Name'
        bot.find_element('xpath', "//input[@ng-reflect-name = 'labelCompanyName']").send_keys(row['Company Name'])
        log_to_file("Campo 'Company Name' preenchido com sucesso.", PATH_LOG)

        # Preenche o campo 'Role in Company'
        bot.find_element('xpath', "//input[@ng-reflect-name = 'labelRole']").send_keys(row['Role in Company'])
        log_to_file("Campo 'Role in Company' preenchido com sucesso.", PATH_LOG)

        # Preenche o campo 'Address'
        bot.find_element('xpath', "//label[text() = 'Address']//following-sibling::input").send_keys(row['Address'])
        log_to_file("Campo 'Address' preenchido com sucesso.", PATH_LOG)

        # Preenche o campo 'Email'
        bot.find_element('xpath', "//input[@ng-reflect-name = 'labelEmail']").send_keys(row['Email'])
        log_to_file("Campo 'Email' preenchido com sucesso.", PATH_LOG)

        # Clica no botão 'Submit'
        bot.find_element('xpath', "//input[@type = 'submit' or @value = 'submit']").click()