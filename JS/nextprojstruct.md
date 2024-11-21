###### next struct
husky
    precommit
        npm run lint
    
    pre-push
        npm run build && npm run test

components
    accordion
    alert
    button
    callout
    cardTabs
    changeField'

    checkbox
    checkbutton
    chip
    confirmationModal
    datepicker
    doughnutChart
    dropdown
    duration
    ellipsis
    error
    fishbone
    forms
    fullscreen
    header
    horizontalBarChart
    iconButton
    layout
    lineChart
    loader
    loadingDots
    logout
    menu
    modal
    pagination
    priorityText
    progressTag
    radio
    searchField
    select
    sideMenu
    spinner
    statusTag
    subheader
    summaryCards
    switch
    table
    tableFilters
    tags
    text
    textArea
    textField
    title
    titleTabs
    toggle
    verticalBarChart

config
context
    hooks
    interfaces
    value

coverage
lib
    config
    plugin

libs
    banking
        hooks
            useBanking.ts
            useBankingContainer.ts
        interfaces
            ibanking.ts
        mocks

        services

        models

        history
        utils
        values
            DEFAULT_BANK_VALUES

    settlements
libs
    banking
        hooks
            useBanking.ts
            useBankingContainer.ts
        interfaces
            ibanking.ts
        mocks

        services
            bankingSvc.ts
        models
        history
        utils
        values
            DEFAULT_BANK_VALUES
    settlements

pages
    banking
        components
            common
            banking
                useBanking.ts
                useBankingCOntainer.ts
                useBankingHistory.ts
        banking
            index.tsx
    api
        axios
            bankingInstance.ts // axios.create({baseUrl, headers})
        base
            bankingBase.ts // base url
        endPoints
            bankingEndpoints.ts

public
    assets
    images
    error.html
    favicon.ico
    logoutPage.html

server
    config
    plugins
    index.ts

tsconfig.server.json

package.json
    ts-node --project tsconfig.server.json server


.eslintrc.json
.npmrc
jest.config.ts
jest.setup.ts
root-ca.cert



libs
    banking
        hooks
            useBanking.ts
            useBankingContainer.ts
        interfaces
            ibanking.ts
        mocks

        services

        models

        history
        utils
        values
            DEFAULT_BANK_VALUES

    settlements