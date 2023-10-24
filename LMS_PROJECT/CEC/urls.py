from django.urls import path
from .views import *


app_name = "CEC"
urlpatterns = [
    # Blog URLs
    path('cec/blogs/', CEC_BlogListCreateView.as_view(), name='blog-list-create'),
    path('cec/blogs/<slug:slug>/', CEC_BlogRetrieveUpdateDeleteView.as_view(), name='blog-retrieve-update-delete'),

    # Comment, Reply, Like and Dislike URLs
    path('cec/blogs/<slug:slug>/comments/', CEC_CommentListCreateView.as_view(), name='comment-list-create'),
    path('cec/blogs/<slug:slug>/comments/<int:comment_id>/', CEC_CommentRetrieveUpdateDeleteView.as_view(), name='comment-retrieve-update-delete'),
    path('cec/blogs/comments/<int:comment_id>/replies/', CEC_ReplyCommentListCreateView.as_view(), name='reply-list-create'),
    path('cec/blogs/comments/<int:comment_id>/replies/<int:reply_id>/', CEC_ReplyCommentRetrieveUpdateDeleteView.as_view(), name='reply-retrieve-update-delete'),
    path('cec/blogs/comments/<int:pk>/like/', CEC_CommentLikeView.as_view(), name='comment-like'),
    path('cec/blogs/comments/<int:pk>/dislike/', CEC_CommentDislikeView.as_view(), name='comment-dislike'),
     path('cec/blogs/comments/<int:comment_id>/replies/<int:pk>/like/', CEC_ReplyCommentLikeView.as_view(), name='reply-comment-like'),
    path('cec/blogs/comments/<int:comment_id>/replies/<int:pk>/dislike/', CEC_ReplyCommentDislikeView.as_view(), name='reply-comment-dislike'),
    ############################# Flutterwave Charge Card Endpoints #################
	# path('cec/flutterwave-charge-card/', CEC_ChargeCardView.as_view()),
	# path('cec/flutterwave-charge-validate/', CEC_ValidateChargeView.as_view())
]
