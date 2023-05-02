from prettyconf import Configuration
import pytest
import allure


@allure.suite("Posts")
@pytest.mark.all
class TestProducts:

    @allure.title("Get Post By Id. Status code 200")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.posts
    def test_get_post_by_id(self, get_posts, props: Configuration, schemas):
        response = get_posts.get_posts(
            path=props("post_id"))
        assert response.status_code == 200
        schemas.get_post.validate(response.json())

    @allure.title("Get All posts. Status code 200")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.posts
    def test_get_all_post(self, get_posts):
        response = get_posts.get_posts(
            path='')
        assert response.status_code == 200

    @allure.title("Create a post. Status code 201")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.posts
    def test_create_post(self, get_posts, props: Configuration):
        body = {
            'id': 1,
            'title': 'This is a example',
            'body': 'This is a body example',
            'userId': '1'
        }
        response = get_posts.post_resource(
            path=props("posts"), body=body)
        assert response.status_code == 201

    @allure.title("Delete a post. Status code 200")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.posts
    def test_delete_post(self, get_posts, props: Configuration):
        response = get_posts.delete_post(
            path=props("post_id"))
        assert response.status_code == 200

    @allure.title("Put Product. Status code 200")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.posts
    def test_update_post(self, get_posts, props: Configuration):
        body = {
            'id': 1,
            'title': 'This is a example from update',
            'body': 'This is a body example',
            'userId': '1'
        }
        response = get_posts.update_post(
            path=props("post_id"), body=body)
        assert response.status_code == 200
