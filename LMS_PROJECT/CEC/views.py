from datetime import datetime
import logging
import string
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework import generics
from .models import *
from .serializers import *
# from tqfe import settings
from django.http import HttpResponse, JsonResponse


class APIResponse:
	@staticmethod
	def send(message, status, err="", data=dict() or list()):
		return Response(
			{"message": message, "status_code": status, "data": data, "error": err}
		)


class CEC_BlogListCreateView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            blogs = Blog.objects.all()
        except Exception:
            return APIResponse.send(
				message="Could not fetch all blogs",
				status=status.HTTP_500_INTERNAL_SERVER_ERROR,
				err=str
			)
        serializer = BlogSerializer(blogs, many=True)
        return APIResponse.send(
				message="Success. Blogs are fetched.",
				status=status.HTTP_200_OK,
				data=serializer.data
			)
            
    def post(self, request):
        serializer = BlogSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return APIResponse.send(
				message="Success. Blog is added!",
				status=status.HTTP_201_CREATED,
				data=serializer.data
			)
        return APIResponse.send(
				message="Serializer error occured.",
				status=status.HTTP_400_BAD_REQUEST,
				err=str(serializer.errors)
			)

class CEC_BlogRetrieveUpdateDeleteView(APIView):
	permission_classes = [AllowAny]
	def get_object(self, slug):
		try:
			return Blog.objects.get(slug=slug)
		except Blog.DoesNotExist:
			raise status.HTTP_404_NOT_FOUND

	def get(self, request, slug):
		try:
			blog = self.get_object(slug)
		except Exception:
			return APIResponse.send(
				message="No such blog with the slug provided.",
				status=status.HTTP_404_NOT_FOUND,
				err="Blog not found."
			)
		serializer = BlogSerializer(blog)
		return APIResponse.send(
				message="Success. Blog is fetched.",
				status=status.HTTP_200_OK,
				data=serializer.data
			)

	def put(self, request, slug):
		try:
			blog = self.get_object(slug)
		except Exception:
			return APIResponse.send(
				message="No such blog with the slug provided.",
				status=status.HTTP_404_NOT_FOUND,
				err="Blog not found."
			)
		serializer = BlogSerializer(blog, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return APIResponse.send(
				message="Success. Blog is updated.",
				status=status.HTTP_200_OK,
				data=serializer.data
			)
		return APIResponse.send(
				message="Serializer error occured.",
				status=status.HTTP_400_BAD_REQUEST,
			   err=str(serializer.errors)
			)

	def delete(self, request, slug):
		try:
			blog = self.get_object(slug)
		except Exception:
			return APIResponse.send(
				message="No such blog with the slug provided.",
				status=status.HTTP_404_NOT_FOUND,
				err="Blog not found."
			)
		blog.delete()
		return APIResponse.send(
				message="Success. Blog is deleted.",
				status=status.HTTP_204_NO_CONTENT
			)


class CEC_CommentListCreateView(APIView):
	permission_classes = [IsAuthenticated]
	def get_object(self, slug):
		try:
			return Blog.objects.get(slug=slug)
		except Blog.DoesNotExist:
			raise status.HTTP_404_NOT_FOUND


	def get(self, request, slug):
		try:
			blog = self.get_object(slug)
		except Exception:
			return APIResponse.send(
				message="No such blog with the slug provided.",
				status=status.HTTP_404_NOT_FOUND,
				err="Blog not found."
			)
		comments = blog.comments.all()
		serializer = CommentSerializer(comments, many=True)
		return APIResponse.send(
				message=f"Success. Comments are fetched for blog with slug {slug}",
				status=status.HTTP_200_OK,
				data=serializer.data
			)
	def post(self, request, slug):
		try:
			blog = self.get_object(slug)
		except Exception:
			return APIResponse.send(
				message=f"No such blog with the slug {slug} provided.",
				status=status.HTTP_404_NOT_FOUND,
				err="Blog not found."
			)

		if not self.request.user.is_authenticated:
			return APIResponse.send(
				message="Unauthenticated user found",
				status=status.HTTP_403_FORBIDDEN
			)
		data = request.data
		data['commentator'] = self.request.user.id #request.user will be used if blog is later outsourced
		data['blog'] = blog.id
		print(request.data)  # Set the 'blog' field explicitly to the ID of the associated blog.
		serializer = CommentSerializer(data=data)
		if serializer.is_valid():
			serializer.save(blog=blog)
			return APIResponse.send(
				message=f"Success. Comment for the blog with slug {slug} is added.",
				status=status.HTTP_201_CREATED,
				data=serializer.data
			)
		return APIResponse.send(
				message="Serializer error occured.",
				status=status.HTTP_400_BAD_REQUEST,
				err=str(serializer.errors)
			)


class CEC_CommentRetrieveUpdateDeleteView(APIView):
	permission_classes = [IsAuthenticated]
	def get_blog_object(self, slug):
		try:
			return Blog.objects.get(slug=slug)
		except Blog.DoesNotExist:
			raise status.HTTP_404_NOT_FOUND

	def get_object(self, comment_id):
		try:
			return Comment.objects.get(id=comment_id)
		except Comment.DoesNotExist:
			raise status.HTTP_404_NOT_FOUND

	def get(self, request, slug, comment_id):
		# blog = self.get_blog_object(slug)
		try:
			comment = self.get_object(comment_id)
		except Exception:
			return APIResponse.send(
				message="No such comment with the id provided.",
				status=status.HTTP_404_NOT_FOUND,
				err=f"Comment with id {comment_id} not found for the blog with slug {slug}"
			)

		serializer = CommentSerializer(comment)
		return APIResponse.send(
				message=f"Success. Comment with {comment_id} is fetched.",
				status=status.HTTP_200_OK,
				data=serializer.data
			)
	def put(self, request, slug, comment_id):
		try:
			blog = self.get_blog_object(slug)
		except Exception:
			return APIResponse.send(
				message="No such blog with the slug provided.",
				status=status.HTTP_404_NOT_FOUND,
				err="Blog not found."
			)
		try:
			comment = self.get_object(comment_id)
		except Exception:
			return APIResponse.send(
				message="No such comment with the id provided.",
				status=status.HTTP_404_NOT_FOUND,
				err=f"Comment with id{comment_id} not found for the blog with slug {slug}"
			)
		data = request.data.copy()
		data['blog'] = blog  # Set the 'blog' field explicitly to the ID of the associated blog.
		serializer = CommentSerializer(comment, data=request.data)
		if serializer.is_valid():
			serializer.save(blog=blog)
			return APIResponse.send(
				message=f"Success. Comment for the blog with slug {slug} is updated.",
				status=status.HTTP_202_ACCEPTED,
			   data=serializer.data
			)
		return APIResponse.send(
				message="Serializer error occured.",
				status=status.HTTP_400_BAD_REQUEST,
				err=str(serializer.errors)
			)

	def delete(self, request, slug, comment_id):
		try:
			comment = self.get_object(comment_id)
		except Exception:
			return APIResponse.send(
				message="No such comment with the id provided.",
				status=status.HTTP_404_NOT_FOUND,
				err=f"Comment with id{comment_id} not found for the blog with slug {slug}"
			)
		comment.delete()
		return APIResponse.send(
				message=f"Success. Comment with id {comment_id} is deleted from blog with slug {slug}.",
				status=status.HTTP_204_NO_CONTENT
			)


class CEC_ReplyCommentListCreateView(APIView):
	permission_classes = [IsAuthenticated]
	def get_object(self, comment_id):
		try:
			return Comment.objects.get(id=comment_id)
		except Comment.DoesNotExist:
			raise status.HTTP_404_NOT_FOUND


	def get(self, request, comment_id):
		try:
			comment = self.get_object(comment_id)
		except Exception:
			return APIResponse.send(
				message="No such comment with the id provided.",
				status=status.HTTP_404_NOT_FOUND,
				err="Comment not found."
			)
		replies = comment.replies.all()
		serializer = ReplyCommentSerializer(replies, many=True)
		return APIResponse.send(
				message=f"Success.Replies are fetched successfully for comment with id {comment_id}",
				status=status.HTTP_200_OK,
				data=serializer.data
			)
	def post(self, request, comment_id):
		try:
			comment = self.get_object(comment_id)
		except Exception:
			return APIResponse.send(
				message="No such comment with the id provided.",
				status=status.HTTP_404_NOT_FOUND,
				err="Blog not found."
			)
		data = request.data
		data['comment'] = comment.id
		serializer = ReplyCommentSerializer(data=data)
		if serializer.is_valid():
			serializer.save(comment=comment)
			return APIResponse.send(
				message=f"Success. Reply for the comment with id {comment_id} is saved.",
				status=status.HTTP_201_CREATED,
				data=serializer.data
			)
		return APIResponse.send(
				message="Serializer error occured.",
				status=status.HTTP_400_BAD_REQUEST,
				err=str(serializer.errors)
			)


class CEC_ReplyCommentRetrieveUpdateDeleteView(APIView):
	permission_classes = [IsAuthenticated]
	def get_comment_bject(self, comment_id):
		try:
			return Comment.objects.get(id=comment_id)
		except Comment.DoesNotExist:
			raise status.HTTP_404_NOT_FOUND


	def get_reply_object(self, reply_id):
		try:
			return ReplyComment.objects.get(id=reply_id)
		except ReplyComment.DoesNotExist:
			raise status.HTTP_404_NOT_FOUND

	def get(self, request, reply_id, comment_id):
		# blog = self.get_blog_object(slug)
		try:
			comment_reply = self.get_reply_object(reply_id)
		except Exception:
			return APIResponse.send(
				message="No such reply with the id provided.",
				status=status.HTTP_404_NOT_FOUND,
				err=f"Reply with id {reply_id} not found."
			)

		serializer = ReplyCommentSerializer(comment_reply)
		return APIResponse.send(
				message="Success.Reply for blog comment {comment_id} is fetched.",
				status=status.HTTP_200_OK,
				data=serializer.data
			)
	def put(self, request, reply_id, comment_id):
		try:
			comment = self.get_comment_bject(comment_id)
		except Exception:
			return APIResponse.send(
				message="No such comment with the id provided.",
				status=status.HTTP_404_NOT_FOUND,
				err="Comment not found."
			)
		try:
			reply_comment = self.get_reply_object(reply_id)
		except Exception:
			return APIResponse.send(
				message="No such reply with the id provided.",
				status=status.HTTP_404_NOT_FOUND,
				err=f"Reply with id{reply_id} not found for the comment with id {comment_id}"
			)
		data = request.data
		data['comment'] = comment.id
		serializer = ReplyCommentSerializer(reply_comment, data=request.data)
		if serializer.is_valid():
			serializer.save(comment=comment)
			return APIResponse.send(
				message=f"Success. Reply for the comment with id {comment_id} is updated.",
				status=status.HTTP_202_ACCEPTED,
			   data=serializer.data
			)
		return APIResponse.send(
				message="Serializer error occured.",
				status=status.HTTP_400_BAD_REQUEST,
				err=str(serializer.errors)
			)

	def delete(self, request, reply_id, comment_id):
		try:
			reply_comment = self.get_reply_object(reply_id)
		except Exception:
			return APIResponse.send(
				message="No such reply with the id provided.",
				status=status.HTTP_404_NOT_FOUND,
				err=f"Reply with id{reply_id} not found for the comment with id {comment_id}"
			)
		reply_comment.delete()
		return APIResponse.send(
				message=f"Success. Reply with id {reply_id} is deleted from comment with id {comment_id}.",
				status=status.HTTP_204_NO_CONTENT
			)



class CEC_CommentLikeView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def patch(self, request, comment_id, *args, **kwargs):
        instance = self.get_object()
        instance.likes += 1
        instance.save()
        return Response({'detail': f'Comment {comment_id} liked successfully'}, status=status.HTTP_200_OK)

class CEC_CommentDislikeView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def patch(self, request, comment_id, *args, **kwargs):
        instance = self.get_object()
        instance.dislikes += 1
        instance.save()
        return Response({'detail': f'comment {comment_id}disliked successfully'}, status=status.HTTP_200_OK)

class CEC_ReplyCommentLikeView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ReplyComment.objects.all()
    serializer_class = ReplyCommentSerializer

    def patch(self, request, *args, comment_id, **kwargs):
        instance = self.get_object()
        instance.likes += 1
        instance.save()
        return Response({'detail': f'Reply comment {comment_id} liked successfully'}, status=status.HTTP_200_OK)

class CEC_ReplyCommentDislikeView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ReplyComment.objects.all()
    serializer_class = ReplyCommentSerializer

    def patch(self, request, comment_id, *args, **kwargs):
        instance = self.get_object()
        instance.dislikes += 1
        instance.save()
        return Response({'detail': f'reply comment {comment_id} disliked successfully'}, status=status.HTTP_200_OK)


# """Payment Views"""
#
# #############################################################
# import base64
# import json
# from Crypto.Cipher import DES3
#
# public_key = settings.FLUTTERWAVE_PUBLIC_KEY
# secret_key = settings.FLUTTERWAVE_SECRET_KEY
# encryption_key = settings.FLUTTERWAVE_ENCRYPTION_KEY
# base_url = settings.FLUTTERWAVE_ENDPOINT
#
# class CEC_ChargeCardView(APIView):
# 	"""View for charging card"""
# 	permission_classes = [IsAuthenticated]
#
# 	#client data needs to be encrypted as required by the Flutterwave
# 	def __encrypt_data(self, payload):
# 		block_size = 8
# 		pad_diff = block_size - (len(payload) % block_size)
# 		cipher = DES3.new(encryption_key.encode(), DES3.MODE_ECB)
# 		plain_text = "{}{}".format(payload, "".join(chr(pad_diff) * pad_diff))
# 		encrypted = base64.b64encode(cipher.encrypt(plain_text.encode()))
# 		return encrypted.decode()
#
# 	#Internal random transaction reference must be generated as required by the flutterwave
# 	def get_transaction_reference(self, length=16):
# 		"""Generate Random String"""
# 		letters = string.ascii_lowercase
# 		result_str = ''.join(random.choice(letters) for i in range(length))
# 		result_str = f'QUESTENCE_{datetime.now().year}_{result_str.upper()}' #QUESTENCE_2023_GKEEUSAQLUTNVRJR" for example
#
# 		return result_str
#
# 	def post(self, request):
# 		"""Post method"""
#
# 		request_user_fullname = f"{request.user.first_name} {request.user.last_name}"
# 		request.data["fullname"] = request_user_fullname
# 		request.data["email"] = request.user.email
# 		request.data["tx_ref"] = self.get_transaction_reference(16)
# 		request.data["authorization"] = {
#                 "mode": "pin",
#                 "pin": request.data["pin"],
#             }
# 		encrypted_data = self.__encrypt_data(json.dumps(request.data))
#
# 		post_data = {
# 			"client": encrypted_data,
# 		}
# 		headers = {
# 			'Authorization': f'Bearer {secret_key}',
# 			'Content-Type': 'application/json'
# 		}
# 		url = base_url + '/charges?type=card'
# 		response = None
# 		try:
# 			response = requests.post(url, json.dumps(post_data), headers=headers)
# 		except Exception as e:
# 			logging.debug(e)
#
#
# 		response = response.json()
# 		if response["status"] != "error":
# 			response = {
# 				"status": response["status"],
# 				"message": response["message"],
# 				"flw_ref": response["data"]["flw_ref"],
# 				"tx_ref": response["data"]["tx_ref"],
# 				"processor_response": response["data"]["processor_response"],
# 				"charged_amount": response["data"]["charged_amount"]
# 			}
# 			return Response(response, status=201)
#
# 		return Response(response, status=400)
#
#
# class  CEC_ValidateChargeView(APIView):
# 	"""View for Validating Card Charge"""
# 	permission_classes = [IsAuthenticated]
#
# 	def post(self, request):
# 		"""POST Request"""
#
# 		data = {
# 			'flw_ref': request.data["flw_ref"],
# 			'otp': request.data["otp"]
# 		}
#
#
# 		headers = {
# 			'Authorization': f'Bearer {secret_key}',
# 			'Content-Type': 'application/json'
# 		}
#
# 		url = base_url + '/validate-charge'
#
# 		response = None
# 		try:
# 			response = requests.post(url, json.dumps(data), headers=headers)
# 		except (Exception, TypeError, ValueError) as e:
# 			logging.debug(e)
#
# 		response = response.json()
#
# 		if response["status"] != "error":
# 			response = {
# 				"status": response["status"],
# 				"message": response["message"],
# 				"flw_ref": response["data"]["flw_ref"],
# 				"tx_ref": response["data"]["tx_ref"],
# 				"charged_amount": response["data"]["charged_amount"]
# 			}
#
# 			return Response(response, status=201)
#
# 		return Response(response, status=400)
