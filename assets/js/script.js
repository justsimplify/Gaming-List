$(document).ready(function () {
    function getRequest(link, callback) {
        Vue.http.get(link).then(function (response) {
            callback(response.data);
            return response.data;
        }, function (error) {
            console.log(error.statusText);
        });
    }

    function replaceElementValue(ele, value) {
        var app = new Vue({
            el: ele,
            data: {
                searchQuery: '',
                message: value
            },
            computed: {
                filteredResources (){
                    if(this.searchQuery) {
                        this.searchQuery = this.searchQuery.toLowerCase();
                        return this.message.filter((item) => {
                            return item.title.toLowerCase().startsWith(this.searchQuery) || item.platform.toLowerCase().startsWith(this.searchQuery) || item.genre.toLowerCase().startsWith(this.searchQuery) || item.editors_choice.toLowerCase().startsWith(this.searchQuery);
                        });
                    } else {
                        return this.message;
                    }
                }
            }
        });
    }

    getRequest("/service/getData/", (data) => {
        replaceElementValue("#vals", data)
    })
});