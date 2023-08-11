link = 'https://en.it-jobs.de/'
driver_path = 'driver/chromedriver'

full_name = 'Oguzhan Kandakoglu'
email = 'oguzhankandakoglu@gmail.com'
resume_path = 'resume/Oguzhan-Kandakoglu-CV.pdf'

place = 'München'
tags = ['Frontend Developer', 'Backend Developer', 'Software Engineer', 'Full Stack Developer', 'Frontend',
        'Backend', 'Java', 'C#', 'JavaScript', 'TypeScript', 'React', 'React Native', 'CSS', 'SCSS', 'Python', 'Node.js']

section_wait = 5
fill_wait = 1

selectors = {

    'cookie_button': '.cmptxt_btn_yes',

    # initial form
    'place_text_box': '#plz-search-bar',
    'tags_text_box': '#tagsearch',
    'expereince_buttons': '.btn-check:not(.languages .btn-check)',
    'match_button': '#match-button',

    # job list
    'job_result': '.result',
    'apply_button': '.btn-action',
    'email_input': '.input-email input',
    'name_input': '.input-name input',
    'attach_resume_button': '.file-upload-button-canvas input',
    'submit_button': '#send-application-btn',

    # wait 1 second

    # load more jobs
    'more_jobs_button': '.load-more-btn',
    'result_list_divider': 'results-page-divider-component',
}
