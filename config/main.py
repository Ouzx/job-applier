link = 'https://en.it-jobs.de/'
driver_path = 'driver/chromedriver'

full_name = 'Oguzhan Kandakoglu'
email = 'oguzhankandakoglu@gmail.com'
resume_path = 'resume/Oguzhan-Kandakoglu-CV.pdf'

place = 'München'
tags = ['Frontend Developer', 'Backend Developer', 'Software Engineer', 'Fullstack-Entwickler/in', 'Full Stack Developer', 'Frontend',
        'Backend', 'Java', 'C#', 'JavaScript', 'TypeScript', 'React', 'React Native', 'CSS', 'SCSS', 'Python', 'Node.js']

selectors = {
    # initial form
    'place_text_box': '#plz-search-bar',
    'tags_text_box': '#tag-search-input',
    'expereince_buttons': '.btn-check:not(.languages .btn-check)',
    'match_button': '#match-button',

    # job list
    'job_result': '.result',
    'apply_button': '.btn-action',
    'email_input': '.input-email input',
    'email_name': '.input-name input',
    'attach_resume_button': '.file-upload-button-canvas input',
    'submit_button': '#send-application-btn',

    # wait 1 second

    # load more jobs
    'more_jobs_button': '.load-more-btn',
    'result_list_divider': 'results-page-divider-component',
}
