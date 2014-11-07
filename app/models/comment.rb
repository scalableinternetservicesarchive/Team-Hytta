class Comment < ActiveRecord::Base
  belongs_to :post
  belongs_to :user
  belongs_to :parent
  validates :post, presence: true
  validates :user, presence: true
end
