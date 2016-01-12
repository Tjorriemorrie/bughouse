module.exports = function (grunt) {

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        copy: {
            fonts: {
                files: [
                    {
                        expand: true,
                        filter: 'isFile',
                        flatten: true,
                        cwd: './bower_components/bootstrap/dist/fonts/',
                        src: '*',
                        dest: './app/static/fonts/',
                    }
                ]
            }
        },

        less: {
            options: {
                compress: true  //minifying the result
            },
            vendor: {
                files: {
                    './app/static/css/vendor.min.css': [
                        './bower_components/bootstrap/dist/css/bootstrap.css',
                        './bower_components/bootstrap/dist/css/bootstrap-theme.css',
                    ]
                }
            },
            masrel: {
                files: {
                    './app/static/css/masrel.min.css': [
                        './assets/less/main.less',
                    ]
                }
            }
        },

		browserify: {
			options: {
				transform: [
					['babelify', {
						presets: ['react', 'es2015', 'stage-0']
					}]
				]
			},

			jsx: {
				files: {
					'./app/static/js/masrel.js': ['./assets/jsx/Index.jsx']
				}
			},
		},

        concat: {
            options: {
                separator: '\n'
            },
            vendor: {
                files: {
                    './app/static/js/vendor.min.js': []
                }
            },
        },

        uglify: {
            options: {
                mangle: true,  // Use if you want the names of your functions and variables unchanged
            },
            jsx: {
                files: {
                    './app/static/js/masrel.min.js': [
                        './app/static/js/masrel.js',
                    ],
                }
            }
        },

        watch: {
            options: {
                spawn: false,
                reload: true,
            },

            less: {
                files: [
                    './assets/less/**/*.less'
                ],
                tasks: ['less:masrel'],
                options: {
                    livereload: true,
                }
            },

            jsx: {
                files: [
                    './assets/jsx/**/*.jsx'
                ],
                tasks: ['browserify:jsx'],
                options: {
                    livereload: true,
                }
            }
        }
    });

    // Load the plugins
    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-less');
	grunt.loadNpmTasks('grunt-browserify');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task(s).
    grunt.registerTask('default', ['copy', 'less', 'browserify', 'concat', 'uglify', 'watch']);
};
