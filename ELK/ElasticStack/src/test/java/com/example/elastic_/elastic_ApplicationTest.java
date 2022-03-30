package com.example.elastic_;

import org.apache.http.HttpHost;
import org.elasticsearch.action.admin.indices.alias.Alias;
import org.elasticsearch.action.admin.indices.create.CreateIndexRequest;
import org.elasticsearch.action.admin.indices.delete.DeleteIndexRequest;
import org.elasticsearch.action.admin.indices.open.OpenIndexRequest;
import org.elasticsearch.action.delete.DeleteRequest;
import org.elasticsearch.action.delete.DeleteResponse;
import org.elasticsearch.action.get.GetRequest;
import org.elasticsearch.action.get.GetResponse;
import org.elasticsearch.action.index.IndexRequest;
import org.elasticsearch.action.index.IndexResponse;
import org.elasticsearch.action.update.UpdateRequest;
import org.elasticsearch.action.update.UpdateResponse;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestHighLevelClient;
import org.elasticsearch.client.indices.CloseIndexRequest;
import org.elasticsearch.common.xcontent.XContentBuilder;
import org.elasticsearch.rest.RestStatus;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import java.io.IOException;
import java.util.Date;
import java.util.Map;

import static org.assertj.core.api.Assertions.assertThat;
import static org.elasticsearch.common.xcontent.XContentFactory.jsonBuilder;

@RunWith(SpringRunner.class)
@SpringBootTest

public class elastic_ApplicationTest {
    @Autowired
    private RestHighLevelClient client;

    // Index명
    private final String INDEX_NAME = "movie_rest";

    // 타입명
    private final String TYPE_NAME = "_doc";

    // 문서 키값
    private final String ID = "1";

    @Before
    public void connection_생성() {
        client = new RestHighLevelClient(
                RestClient.builder(
                        new HttpHost("127.0.0.1", 9200, "http")));
    }

    @After
    public void connection_종료() throws IOException {
        client.close();
    }

    @Test
    public void index_테스트1_생성() throws IOException {

        // 매핑정보
        XContentBuilder indexBuilder = jsonBuilder()
                .startObject()
                .startObject(TYPE_NAME)
                .startObject("properties")
                .startObject("movieCd")
                .field("type", "keyword")
                .field("store", "true")
                .field("index_options", "docs")
                .endObject()
                .startObject("movieNm")
                .field("type", "text")
                .field("store", "true")
                .field("index_options", "docs")
                .endObject()
                .startObject("movieNmEn")
                .field("type", "text")
                .field("store", "true")
                .field("index_options", "docs")
                .endObject()
                .endObject()
                .endObject()
                .endObject();

        // 매핑 설정
        CreateIndexRequest request = new CreateIndexRequest(INDEX_NAME);
        request.mapping(TYPE_NAME, indexBuilder);

        // Alias 설정
        String ALIAS_NAME = "moive_auto_alias";
        request.alias(new Alias(ALIAS_NAME));

        boolean acknowledged = client.indices()
                .create(request, RequestOptions.DEFAULT)
                .isAcknowledged();

        assertThat(acknowledged).isEqualTo(true);
    }

    @Test
    public void index_테스트2_닫기() throws IOException{

        CloseIndexRequest requestClose = new CloseIndexRequest(INDEX_NAME);

        boolean acknowledged  = client.indices().close(requestClose, RequestOptions.DEFAULT).isAcknowledged();

        assertThat(acknowledged).isEqualTo(true);
    }

    @Test
    public void index_테스트3_오픈() throws IOException{

        OpenIndexRequest requestOpen = new OpenIndexRequest(INDEX_NAME);

        boolean acknowledged  = client.indices().open(requestOpen, RequestOptions.DEFAULT).isAcknowledged();

        assertThat(acknowledged).isEqualTo(true);
    }

    @Test
    public void index_테스트4_삭제() throws IOException {

        DeleteIndexRequest request = new DeleteIndexRequest(INDEX_NAME);

        boolean acknowledged = client.indices()
                .delete(request, RequestOptions.DEFAULT)
                .isAcknowledged();

        assertThat(acknowledged).isEqualTo(true);
    }

    @Test
    public void index_테스트1_insert() throws IOException {

        IndexRequest request = new IndexRequest(INDEX_NAME,TYPE_NAME, ID);

        request.source(jsonBuilder()
                .startObject()
                .field("movieCd", "20173732")
                .field("movieNm", "살아남은 아이")
                .field("movieNmEn", "Last Child")
                .endObject()
        );

        IndexResponse response = client.index(request, RequestOptions.DEFAULT);
        String id = response.getId();
        RestStatus status = response.status();

        assertThat(id).isEqualTo("1");
        assertThat(status).isEqualTo(RestStatus.CREATED);
    }

    @Test
    public void index_테스트2_get() throws IOException {

        GetRequest request = new GetRequest( INDEX_NAME, TYPE_NAME,ID);

        GetResponse response = client.get(request, RequestOptions.DEFAULT);

        Map<String, Object> sourceAsMap = response.getSourceAsMap();
        String movieCd = (String) sourceAsMap.get("movieCd");
        String movieNm = (String) sourceAsMap.get("movieNm");
        String movieNmEn = (String) sourceAsMap.get("movieNmEn");

        assertThat(movieCd).isEqualTo("20173732");
        assertThat(movieNm).isEqualTo("살아남은 아이");
        assertThat(movieNmEn).isEqualTo("Last Child");
    }

    @Test
    public void index_테스트3_update() throws IOException {

        XContentBuilder builder = jsonBuilder()
                .startObject()
                .field("createdAt", new Date())
                .field("prdtYear", "2018")
                .field("typeNm", "장편")
                .endObject();

        UpdateRequest request = new UpdateRequest(INDEX_NAME, TYPE_NAME, ID).doc(builder);

        UpdateResponse updateResponse = client.update(request, RequestOptions.DEFAULT);
        RestStatus status = updateResponse.status();

        assertThat(status).isEqualTo(RestStatus.OK);
    }

    @Test
    public void index_테스트4_delete() throws IOException {

        DeleteRequest request = new DeleteRequest(INDEX_NAME, TYPE_NAME, ID);
        DeleteResponse deleteResponse = client.delete(request, RequestOptions.DEFAULT);

        RestStatus status = deleteResponse.status();
        assertThat(status).isEqualTo(RestStatus.OK);
    }
}
