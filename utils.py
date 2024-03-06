from PIL import Image, ImageOps


def fetch_product_image(product_id, should_resize=True, img_width=100, img_height = 150):
    
    img_path = 'results/images/'+product_id+'.jpeg'
    product_image = Image.open(img_path)
    
    if should_resize:
        product_image = product_image.resize((img_width, img_height), Image.ANTIALIAS)
    product_image = ImageOps.expand(product_image, 2)
        
    return product_image    


def fetch_recommendations(customer_info):
    
    combined_recommendations = customer_info.combined_rcmnds.values
    tfrs_recommendations = customer_info.tfrs_rcmnds.values
    image_recommendations = customer_info.image_rcmnds.values
    text_recommendations = customer_info.text_rcmnds.values
    feature_recommendations = customer_info.feature_rcmnds.values

    return image_recommendations, text_recommendations, feature_recommendations, tfrs_recommendations, combined_recommendations

def fetch_recommendation_scores(customer_info):
    
    combined_scores = customer_info.combined_scores.values
    tfrs_scores = customer_info.tfrs_scores.values
    image_scores = customer_info.image_scores.values
    text_scores = customer_info.text_scores.values
    feature_scores = customer_info.feature_scores.values

    return image_scores, text_scores, feature_scores, tfrs_scores, combined_scores

def fetch_recommendation_images(image_recommendations, text_recommendations, feature_recommendations, tfrs_recommendations, combined_recommendations):
    
    combined_images = [fetch_product_image(str(i)) for i in combined_recommendations]
    tfrs_images = [fetch_product_image(str(i)) for i in tfrs_recommendations]
    image_images = [fetch_product_image(str(i)) for i in image_recommendations]
    text_images = [fetch_product_image(str(i)) for i in text_recommendations]
    feature_images = [fetch_product_image(str(i)) for i in feature_recommendations]
    
    return image_images, text_images, feature_images, tfrs_images, combined_images


def fetch_recommendation_features(dataframe, image_recommendations, text_recommendations, feature_recommendations, tfrs_recommendations, combined_recommendations):
    
    combined_features = dataframe[dataframe.article_id.isin(combined_recommendations)][['product_type_name', 'colour_group_name', 'department_name']]
    tfrs_features = dataframe[dataframe.article_id.isin(tfrs_recommendations)][['product_type_name', 'colour_group_name', 'department_name']]
    image_features = dataframe[dataframe.article_id.isin(image_recommendations)][['product_type_name', 'colour_group_name', 'department_name']]
    text_features = dataframe[dataframe.article_id.isin(text_recommendations)][['product_type_name', 'colour_group_name', 'department_name']]
    feature_features = dataframe[dataframe.article_id.isin(feature_recommendations)][['product_type_name', 'colour_group_name', 'department_name']]
    
    return image_features, text_features, feature_features, tfrs_features, combined_features
    

def fetch_recommendation_descriptions(dataframe, image_recommendations, text_recommendations, feature_recommendations, tfrs_recommendations, combined_recommendations):
    
    combined_descriptions = dataframe[dataframe.article_id.isin(combined_recommendations)].detail_desc
    tfrs_descriptions = dataframe[dataframe.article_id.isin(tfrs_recommendations)].detail_desc
    image_descriptions = dataframe[dataframe.article_id.isin(image_recommendations)].detail_desc
    text_descriptions = dataframe[dataframe.article_id.isin(text_recommendations)].detail_desc
    feature_descriptions = dataframe[dataframe.article_id.isin(feature_recommendations)].detail_desc
    
    return image_descriptions, text_descriptions, feature_descriptions, tfrs_descriptions, combined_descriptions
