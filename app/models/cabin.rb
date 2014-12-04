class Cabin < ActiveRecord::Base
	belongs_to :user
	has_many :posts, dependent: :destroy
	has_many :photoalbums, dependent: :destroy
	validates :user, presence: true
end
