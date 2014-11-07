class PostsController < ApplicationController
  before_action :set_post, only: [:show, :edit, :update, :destroy]
  respond_to :html, :json

  def index
    @posts = Post.all
    respond_with @posts
  end

  def show
    respond_with @post
  end

  def new
    @post = Post.new
    respond_with @post
  end

  def edit
    respond_with @cabin
  end

  def create
    @post = Post.new(post_params)
    @post.user = current_user
    @post.save
    respond_with @post
  end

  def update
    @post.update(post_params)
    respond_with @post
  end

  def destroy
    @post.destroy
    respond_with @post
  end

  private
    def set_post
      @post = Post.find(params[:id])
    end

    def post_params
      params.require(:post).permit(:title, :message, :cabin_id)
    end
end
