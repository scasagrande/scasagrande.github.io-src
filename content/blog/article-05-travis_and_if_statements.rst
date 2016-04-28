Travis CI and If Statements
###########################

:date: April 28, 2016
:author: Steven Casagrande
:tags: travis, bash

So the other day at work (seems to be a trend in my posts) I was investigating a problem that we noticed with one of our project's TravisCI builds. Specifically, we found that a step under :code:`script` had failed, but the overall build still passed! Very curious problem indeed, and of course needs to be immediately fixed.

Let's take a look at a similar offending code block:

.. code-block:: yaml

    script:
        - 'if [ ${TRAVIS_SECURE_ENV_VARS} = "true" ]; then
              docker run project-container "npm run test";
              docker run project-container "npm run test:lint";
              docker-compose run ui-tests;
          else
              npm run test;
              npm run test:lint;
          fi'

Before we continue, I'd like to point out that I did not write this :code:`if` block. In fact, here is what I had just weeks before:

.. code-block:: yaml

    script:
        - docker run project-container "npm run test"
        - docker run project-container "npm run test:lint"
        - docker-compose run ui-tests

But, because people wanted to be able to work in forks on Github, decisions were made to disable tests to accommodate the workflow. That's another topic for another day. The important part for this story is that the Travis configuration file was changed to accommodate this.

What I noticed was that an error was being generated during the :code:`docker run project-container "npm run test"` step. This is a big problem; the build should be flagged as a failure if this happens!

So I stopped to think for a bit. Travis is clearly checking for non-zero exit codes to determine when to fail or error a build. But the question is, when does this check occur, and why was it working just fine before the :code:`if` statement was introduced? Well then it hit me. The :code:`if` block is executed entirely as one command, and the exit code is checked after it is finished.

With this in mind, I did some quick experimenting. I made two files, each simply with either :code:`exit 0;` or :code:`exit 1;` to simulate commands that either pass or fail. Then, I ran the following in my terminal:

.. code-block:: Console

    $ if [ 0 = 0 ]; then ./fail.sh; ./pass.sh; fi
    $ echo "$?"
    0

Where :code:`$?` is the exit code of the last run command. It printed out a :code:`0`! Ah ha! This is what Travis will see, and so the build passes.

So there are two main solutions here. We need to make sure that Travis knows to fail the build when something goes wrong. Either your :code:`if` block needs to be in its own file with :code:`set -ev` at the top (to stop the script when an error occurs), like so:

.. code-block:: Bash
    :linenos: table

    #!/bin/bash

    set -ev

    if [ ${TRAVIS_SECURE_ENV_VARS} = "true" ]; then
        docker run project-container "npm run test";
        docker run project-container "npm run test:lint";
        docker-compose run ui-tests;
    else
        npm run test;
        npm run test:lint;
    fi

    exit 0;

Or, you can directly call the command to terminate the Travis job by changing the block in your :code:`.travis.yml` file like so:

.. code-block:: Bash
    :linenos: table

    if [ ${TRAVIS_SECURE_ENV_VARS} = "true" ]; then
        docker run project-container "npm run test" || travis_terminate 1;
        docker run project-container "npm run test:lint" || travis_terminate 1;
        docker-compose run ui-tests || travis_terminate 1;
    else
        npm run test || travis_terminate 1;
        npm run test:lint || travis_terminate 1;
    fi

So the moral of the story is, don't put :code:`if` statements in your :code:`.travis.yml` file if you care about the exit status.
